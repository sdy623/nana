import re

from nonebot import CommandSession, CommandGroup
from nonebot import on_natural_language, NLPSession, IntentCommand
from nonebot.helpers import render_expression as expr
from jieba import posseg
from nana import nlp, logger
from nana.command import allow_cancellation
from nana.plugins.weather.data_source import get_weather
from . import expressions as e

__plugin_name__ = '天气'

w = CommandGroup('weather')


@w.command('weather', aliases=('weather', '天气', '天气预报', '查天气'),
           only_to_me=False)
async def weather_command(session: CommandSession):
    location = session.get('location', prompt=expr(e.WHERE))
    if location.province and not location.city and not location.district:
        # there is no city or district, ask the user for more info!
        if 'location_more' in session.state:
            del session.state['location_more']
        session.get('location_more', prompt=expr(e.WHERE_IN_PROVINCE,
                                                 location.province))

    logger.debug(f'Location: {location}')
    final_loc = location.heweather_format()
    weathers = await get_weather(final_loc)
    if len(weathers) > 1:
        await session.send(f'查询到 {len(weathers)} 个同名地区')
    elif len(weathers) == 0:
        session.finish(f'没有查询到{location.short_format()}的天气哦')

    for weather in weathers:
        basic = weather['basic']
        location_name = basic['admin_area']
        if basic['admin_area'] != basic['parent_city']:
            location_name += basic['parent_city']
        if basic['parent_city'] != basic['location']:
            location_name += basic['location']
        report_now = expr(e.REPORT_NOW, **weather['now'])
        report_today = expr(
            e.REPORT_FUTURE_DAY,
            '今天',
            **weather['daily_forecast'][0]
        )
        report_tomorrow = expr(
            e.REPORT_FUTURE_DAY,
            '明天',
            **weather['daily_forecast'][1]
        )
        report_after_tomorrow = expr(
            e.REPORT_FUTURE_DAY,
            '后天',
            **weather['daily_forecast'][2]
        )
        await session.send(f'{location_name}\n\n'
                           f'{report_now}\n\n'
                           f'{report_today}\n\n'
                           f'{report_tomorrow}\n\n'
                           f'{report_after_tomorrow}')


@weather_command.args_parser
@allow_cancellation
async def _(session: CommandSession):
    striped_text_arg = session.current_arg_text.strip()
    if not striped_text_arg:
        # ignore empty argument
        return

    if session.is_first_run:
        session.current_key = 'location'

    if session.current_key == 'location':
        location = await nlp.parse_location(striped_text_arg)
        if any([location.province, location.city, location.district]):
            session.state['location'] = location
        else:
            session.pause('无法识别你输入的城市哦，请重新输入')
    elif session.current_key == 'location_more':
        patched_loc = await nlp.parse_location(striped_text_arg)
        location: nlp.Location = session.state.get('location')
        assert location
        # merge location
        location.province = location.province or patched_loc.province
        location.city = location.city or patched_loc.city
        location.district = location.district or patched_loc.district
        session.state['location'] = location
    else:
        session.state[session.current_key] = striped_text_arg


@on_natural_language(keywords={'天气'})
async def _(session: NLPSession):
    # 去掉消息首尾的空白符
    stripped_msg = session.msg_text.strip()
    # 对消息进行分词和词性标注
    words = posseg.lcut(stripped_msg)

    city = None
    # 遍历 posseg.lcut 返回的列表
    for word in words:
        # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
        if word.flag == 'ns':
            # ns 词性表示地名
            city = word.word
            break

    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'weather', current_arg=city or '')

# @on_natural_language({'雨', '雪', '晴', '阴', '冰雹', '雾'})
# async def _(session: NLPSession):
#     text = session.msg_text.strip()
#     from pprint import pprint
#     pprint(await nlp.lexer(text))
#
#     # if not ('?' in session.msg_text or '？' in session.msg_text):
#     #     return None
#     # return NLPResult(90.0, ('weather', 'weather'), {})
