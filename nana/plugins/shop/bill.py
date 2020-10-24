from nonebot import CommandSession, MessageSegment
from nonebot.typing import Context_T
from .conf import settings
from nana import dt
from . import cg
from . import da
from .helpers import inject_account
from .models import Account
import os
import random


@cg.command('bill', aliases=['结账', '下单'],
            only_to_me=False)
@inject_account
async def _(session: CommandSession):
    account = session.state['account']
    total = []
    #111111
    with open(settings.SHOPPING_CARS, mode='r', encoding='utf-8') as f1, \
    open(settings.SHOPPING_CARS_TMP, mode='w', encoding='utf-8') as f2,  \
    open(settings.MAIDAODE_LIST_TMP, mode='a', encoding='utf-8') as f3:    
        for line in f1:
            user, commodity, price, nums = line.strip().split('|')
            if user == session.ctx["sender"]["nickname"]:
                f3.write(f"{user}|{commodity}|{price}|{nums}\n")
                total.append(int(price) * int(nums))
            else:
                f2.write(line)
    os.remove(settings.SHOPPING_CARS)
    os.rename(settings.SHOPPING_CARS_TMP, settings.SHOPPING_CARS)
    money = sum(total)
    if account.total_coins < money:
        with open(settings.MAIDAODE_LIST_TMP, mode='r', encoding='utf-8') as f3 , \
        open(settings.SHOPPING_CARS, mode='a', encoding='utf-8') as f1:
            for line in f3:
                f1.write(line)
        os.remove(settings.MAIDAODE_LIST_TMP)
        retext='余额不足'
        session.finish(MessageSegment.image(account.avatar_url) +
        '\n'+
        f'{retext}\n')

    else:
        with open(settings.MAIDAODE_LIST_TMP, mode='r', encoding='utf-8') as f3 , \
        open(settings.MAIDAODE_LIST, mode='a', encoding='utf-8') as f4:
            for line in f3:
                f4.write(line)
        os.remove(settings.MAIDAODE_LIST_TMP)
        total_coins = account.total_coins - int(money)
        await da.update(account,total_coins=total_coins)
        retext='购买成功'+'\n'+'总价 '+str(money)+'金币'
        session.finish(MessageSegment.image(account.avatar_url) +'\n'+
        f'{retext}\n')

async def bill(ctx: Context_T, account: Account) -> str:
        total = []
        with open(settings.SHOPPING_CARS, mode='r', encoding='utf-8') as f1, \
        open(settings.SHOPPING_CARS_TMP, mode='w', encoding='utf-8') as f2:
            for line in f1:
                user, commodity, price, nums = line.strip().split('|')
                if user == ctx["sender"]["nickname"]:
                    total.append(float(price) * int(nums))
                else:
                    f2.write(line)
        os.remove(settings.SHOPPING_CARS)
        os.rename(settings.SHOPPING_CARS_TMP, settings.SHOPPING_CARS)
        money = sum(total)
        if account.total_coins< money:
            retext='余额不足'
            return (MessageSegment.image(account.avatar_url) +
            f'\n'
            f'{retext}\n')
        else:
            os.rename(settings.MAIDAODE_LIST_TMP, settings.MAIDAODE_LIST)
            total_coins = account.total_coins - money
            await da.update(account,total_coins=total_coins)
            retext='购买成功'
            return (MessageSegment.image(account.avatar_url) +
            f'\n'
            f'{retext}\n')