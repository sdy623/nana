import random
from datetime import timedelta

from nonebot import CommandSession, MessageSegment
from nana.command import allow_cancellation
from .conf import settings
from nana import dt
from . import cg
from . import da
from .helpers import inject_account
@cg.command('store', aliases=['商城'], only_to_me=False)
@inject_account
async def store_command(session: CommandSession):
    account = session.state['account']
    reply = str(MessageSegment.image(account.avatar_url))
    item_list=f'欢迎 {session.ctx["sender"]["nickname"]} 来到nana的神秘商店\n'\
              f'编号\t\t商品\t\t金额\n'
    with open(settings.GOODS_LIST, mode='r', encoding='utf-8') as f:
        for line in f:
            #print(line.strip())
            iid, commodity, price = line.strip().split('|')
            ass=iid+'\t'+commodity+'\t'+price+'\n'
            item_list+=iid+'\t'+commodity+'\t'+price+'\n'
    if session.ctx['message_type'] != 'private':
        reply += '\n' + str(MessageSegment.at(session.ctx['user_id']))
    '''
    reply += f'\n欢迎 {session.ctx["sender"]["nickname"]} 来到nana的神秘商店\n' \
        '本店有以下商品\n'\
        '1 测试\n'\
        '2 测试\n'\
        '3 测试\n'
    '''
    #await buy(item)
    await session.send(item_list)


async def goods_list(session: CommandSession):
    """
    打印商品列表
    :return:
    """
    item_list=f'\n欢迎 {session.ctx["sender"]["nickname"]} 来到nana的神秘商店\n',\
              f'商品'+'\t'+'金额'+'\n'
    with open(settings.GOODS_LIST, mode='r', encoding='utf-8') as f:
        for line in f:
            #print(line.strip())
            commodity, price = line.strip().split('|')
            ass=commodity+'\t'+price+'\n'
            item_list+=commodity+'\t'+price+'\n'
    return item_list

@store_command.args_parser
@allow_cancellation

async def _(session: CommandSession):
    user=session.ctx["sender"]["nickname"]
    striped_text_arg = session.current_arg_text.strip()
    if not striped_text_arg:
        # ignore empty argument
        return

    session.current_key = 'item'
#####
    if session.current_key == 'item':
        item = striped_text_arg
        nums = 1
        with open(settings.GOODS_LIST, mode='r', encoding='utf-8') as f1, \
             open(settings.SHOPPING_CARS, mode='a', encoding='utf-8') as f2:
             ass='null'
             for line in f1:
                iid, commodity, price = line.strip().split('|')
                if commodity == item:
                    f2.write(f"{user}|{commodity}|{price}|{nums}\n")
                    # print(f'{commodity}已加入购物车！')
                    ass=user+'已将'+commodity+'加入购物车'+'\n'
                    ass+='以上内容用于测试，不代表最终上线品质'
                    ass=str(ass)
                    await session.send(ass)
                    break
                                            
                elif iid == item:
                    f2.write(f"{user}|{commodity}|{price}|{nums}\n")
                    # print(f'{commodity}已加入购物车！')
                    ass=user+'已将'+commodity+'加入购物车'+'\n'
                    ass+='以上内容用于测试，不代表最终上线品质'
                    ass=str(ass)
                    await session.send(ass)
                    break
             if ass=='null':    
                session.pause('无法识别你输入的商品哦，请重新输入')
        
    session.state[session.current_key] = striped_text_arg
    session.finish()
            


