import random
from nonebot import on_command, CommandSession
@on_command('xml')
async def xml(session: CommandSession):
    a='[CQ:xml,data='+session.state.get('message')+']'
    await session.send(a)