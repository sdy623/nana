import random
from nonebot import on_command, CommandSession
import json
from aiocqhttp.message import escape, unescape
__plugin_name__ = 'json代码转卡片'
@on_command('json', only_to_me=False)
async def card(session: CommandSession):
    session.state.get('message')
    message = session.state.get('message')
    message = json.dumps(message)
    cq_message='[CQ:json,data='+message+']'
    await session.send(cq_message or session.current_arg) 
