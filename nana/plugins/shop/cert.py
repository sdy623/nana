from nonebot import CommandSession, MessageSegment
from nonebot.typing import Context_T
from .conf import settings
from . import cg
from .helpers import inject_account
from .models import Account


@cg.command('cert', aliases=['购物车', '我的购物车'],
            only_to_me=False)
@inject_account
async def _(session: CommandSession):
    account = session.state['account']
    session.finish(format_account(session.ctx, account))


def format_account(ctx: Context_T, account: Account) -> str:
    swih=0
    total = []
    certcar=f'{ctx["sender"]["nickname"]}的购物车\n'\
            f'商品'+'\t'+'金额'+'\n'
            
    with open(settings.SHOPPING_CARS, mode='r', encoding='utf-8') as f:
        for line in f:
            user, commodity, price, nums = line.strip().split('|')
            if user == ctx["sender"]["nickname"]:
                certcar+=commodity+'\t'+price+'\n'
                swih=1
                total.append(float(price) * int(nums))
        if swih==0:
            certcar='你的购物车已清空'
        if swih==1:
            money = sum(total)
            certcar+='总价: '+str(money)+'金币'
    return (MessageSegment.image(account.avatar_url) +
            f'\n'
            f'{certcar}\n')