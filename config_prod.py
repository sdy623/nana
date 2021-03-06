from os import path

from nonebot.default_config import *

NICKNAME = ['nana', 'nana酱','ななちゃん']
COMMAND_START = {'', '/', '!', '／', '！'}
COMMAND_SEP = {'/', '.'}
SUPERUSERS = {1010378863}
SESSION_RUN_TIMEOUT = timedelta(seconds=20)


# 用户取消交互时的回复
SESSION_CANCEL_EXPRESSION = (
    '好的',
    '好的吧',
    '好吧，那nana酱就不打扰啦',
    '那nana酱先不打扰小主人啦',
)

#当有命令会话正在运行时，给用户新消息的回复
SESSION_RUNNING_EXPRESSION='nana酱在为你思考啊,等一下再说吧。'

# 数据文件夹
DATA_FOLDER = path.join(path.dirname(__file__), 'data')

# 数据库 URL
DATABASE_URL = 'postgresql://postgres@/nana'

# 消息采集器 dump 频率
MESSAGE_COLLECTOR_DUMP_FREQ = 'H'

# aiocache 配置
AIOCACHE_DEFAULT_CONFIG = {
    'cache': 'aiocache.SimpleMemoryCache',
    'serializer': {
        'class': 'aiocache.serializers.PickleSerializer'
    }
}

# 使用手册图片地址
#MANUAL_IMAGE_URL_FORMAT = 'https://raw.githubusercontent.com/sdy623/nana/master/manual/screenshots/{}.png' #国际地址
MANUAL_IMAGE_URL_FORMAT = 'https://gitee.com/vantdn/nana/raw/master/manual/screenshots/{}.png'#国内地址
# 允许和炸毛互动的群
GROUPS_TO_PLAY_WITH_ZHAMAO = []

# API url:https://saucenao.com/search.php
SAUCENAO_KEY = '278e48d62f4711b2f03c57c17d14601aff56eaeb'

# 百度 AIP
BAIDU_AIP_APP_ID = '21547102'
BAIDU_AIP_API_KEY = '48nht8TNOZ4dihK20ggb3mvU'
BAIDU_AIP_SECRET_KEY = 'lVr9VITGSU4D3hI9CDTcvZZuF4jSbKje'

# 语言云
LTP_CLOUD_API_KEY = ''

# 图灵机器人
TULING_API_KEY = ''

# API url:https://api.lolicon.app/#/setu
LOLICONAPI = "987173995f547e9a968025" # key

# 和风天气
HEWEATHER_KEY = '23541c46430240e39c78f83623ffb000'

# 聚合数据
JUHE_JOKE_API_KEY = ''  # 笑话大全
JUHE_IDIOM_API_KEY = ''  # 成语词典

#腾讯api
APP_ID = '2156382408'
APP_KEY = 'HjkrOoPD5C6BCFf0'
BAYES = True

# Bool类
CONFIGURATION_WIZARD: bool = True # 设置每次运行时是否需要确认运行配置向导
XDEBUG: bool = True # 日志是否输出DEBUG
#BUILTIN_PLUGINS = True # 是否加载nonebot的默认插件
CEICONLYCN: bool = True # 是否只报道国内地震
RECOMMENDER_MUSIC: bool = False # 音乐推荐功能的回复是否显示推荐者
PLAYLIST_MUSIC: bool = True # 音乐推荐功能的回复是否显示来源歌单
MORE_COMPLEX: bool = False # 是否提供更加复杂的计算库