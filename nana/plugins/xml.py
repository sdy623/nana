import random
from nonebot import on_command, CommandSession
import json
from aiocqhttp.message import escape, unescape
__plugin_name__ = 'xml代码转卡片'
@on_command('xml', only_to_me=False)
async def card(session: CommandSession):   
    session.state.get('message')
    message = session.state.get('message')
    cq_message='[CQ:xml,data='+message+']'
    await session.send(cq_message or session.current_arg)