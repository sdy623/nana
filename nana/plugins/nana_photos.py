from urllib.parse import quote_plus
from random import choice
from nonebot import MessageSegment
from nonebot import on_command, CommandSession, get_loaded_plugins
from nonebot import on_natural_language, NLPSession, IntentCommand
KEYWORDS = ['照片', '玉照', '模样', '样子', '长什么样', '形象']
__plugin_name__ = 'nana照片'
urls = ['https://i.loli.net/2020/09/02/vjI5ZoeVDHdR4Mi.jpg', 'https://i.loli.net/2020/09/05/J3YPBEhSqk9OiKv.jpg', 'https://i.loli.net/2020/09/05/RXg7FvknbtS9HUj.jpg', 'https://i.loli.net/2020/09/05/n2Yv945OVGKqLca.jpg','https://i.loli.net/2020/09/05/M4uJn1K8F9ibcwE.jpg','https://i.loli.net/2020/09/05/sxCzlOcLfqPRy5h.jpg']
url=choice(urls)
@on_command('photo', aliases=['photos', 'photo', 'syashin', *KEYWORDS],
            only_to_me=False)
async def _(session: CommandSession):
    await send_nana_image(session)
async def send_nana_image(session: CommandSession) -> None:
    #url_format = session.bot.config.MANUAL_IMAGE_URL_FORMAT
    await session.send(MessageSegment.image(url))
@on_natural_language(KEYWORDS)
async def _(session: NLPSession):
    miss = max(0, len(session.msg_text) - 4) * 5
    return IntentCommand(100.0 - miss, 'photo')