from nonebot import CommandGroup
__table_args__ = {'extend_existing': True}
__plugin_name__ = '商城'

cg = CommandGroup('store')

from . import account, huojia, bill, cert, maidaode
from nana import dt
from . import cg
from . import da
from .helpers import inject_account