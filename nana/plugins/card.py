import random
from nonebot import on_command, CommandSession
import json
from aiocqhttp.message import escape, unescape
__plugin_name__ = '代码转卡片'
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError:
    return False
  return True 
@on_command('card')
async def card(session: CommandSession):
    session.state.get('message')
    message = session.state.get('message')
    #xml 消息去转义
    if is_json(message) == False:
      cq_message='[CQ:xml,data='+message+']'
      await session.send(unescape(cq_message, escape_comma= True) or session.current_arg)
    else:
      cq_message='[CQ:json,data='+message+']'
      await session.send(cq_message or session.current_arg)
      
