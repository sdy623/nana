# -*- coding: utf-8 -*-
# Author:w k


# 点赞 需要pro

#from . import other
#import nonebot as rcnb
from collections import deque
from nonebot import on_command, CommandSession

IS_LIKE = deque()


@on_command('send_like', aliases={'点赞', '赞我'})
async def like(session: CommandSession):
    session.event['times'] = 10
    await session.bot.send_like(**session.event)
    msg = f'[CQ:at,qq={session.event["user_id"]}]已经给你赞了10次了,记得回赞哦。'
    if session.event["user_id"] in IS_LIKE:
        msg = f'[CQ:at,qq={session.event["user_id"]}]今天已经赞过你啦！'
    IS_LIKE.append(session.event["user_id"])
    await session.finish(msg)
