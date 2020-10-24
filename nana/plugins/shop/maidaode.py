from nonebot import CommandSession, MessageSegment
from nonebot.typing import Context_T
from .conf import settings
from . import cg
from .helpers import inject_account
from .models import Account


@cg.command('maidaode', aliases=['买到的宝贝', '买到的','我买到的宝贝'],
            only_to_me=False)
@inject_account
async def _(session: CommandSession):
    account = session.state['account']
    session.finish(mai_daode(session.ctx, account))


def mai_daode(ctx: Context_T, account: Account) -> str:
    maidaode=f'{ctx["sender"]["nickname"]}买到的宝贝\n'
    with open(settings.MAIDAODE_LIST, mode='r', encoding='utf-8') as f:
        for line in f:
            user, commodity, price, nums = line.strip().split('|')
            if user == ctx["sender"]["nickname"]:
                maidaode+=commodity+'\t'+price+'\n'
            else:
                maidaode+='还不买些东西吗'
    return (MessageSegment.image(account.avatar_url) +
            f'\n'
            f'{maidaode}\n')