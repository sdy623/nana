import random

from nonebot import NoneBot

from nana.aio import requests


async def get_joke(bot: NoneBot):
    resp = await requests.post(
        'http://v.juhe.cn/joke/content/text.php',
        # 注：这里请使用 POST 请求，官网上说的 GET 请求无效
        data={
            'key': bot.config.JUHE_JOKE_API_KEY,
            'page': 1,
            'pagesize': 20,
        }
    )

    payload = await resp.json()
    if not payload or not isinstance(payload, dict):
        return '抱歉，没有新段子了～'

    info = ''
    if payload['error_code'] == 0:
        try:
            jokes = [j['content'] for j in payload['result']['data']]
            if jokes:
                info = random.choice(jokes)
                info = info.replace('&nbsp;', '').strip()
        except KeyError:
            pass

    return info or '暂时没有笑话可以讲哦'


"""
请求参数说明：
key       必填  api_key
page      选填  当前页数,默认1
pagesize  选填  每次返回条数,默认1,最大20

JSON返回示例：
{
    "error_code": 0,
    "reason": "Success",
    "result": {
        "data": [
            {
                "content": "女生分手的原因有两个，\r\n一个是：闺蜜看不上。另一个是：闺蜜看上了。",
                "hashId": "607ce18b4bed0d7b0012b66ed201fb08",
                "unixtime": 1418815439,
                "updatetime": "2014-12-17 19:23:59"
            },
            {
                "content": "老师讲完课后，问道\r\n“同学们，你们还有什么问题要问吗？”\r\n这时，班上一男同学举手，\r\n“老师，这节什么课？”",
                "hashId": "20670bc096a2448b5d78c66746c930b6",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "“老公，结婚前你不是常对我说，我是你的女神吗？”\r\n“老婆，现在你总该看出来，自从结婚后，我成了一个无神论者。”",
                "hashId": "1a0b402983f22b7ad6ff38787e238f6d",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "昨天下班坐公交车回家，白天上班坐着坐多了想站一会儿，\r\n就把座位让给了一个阿姨，阿姨道谢一番开始和我聊天，聊了挺多的。
                \r\n后来我要下车了，阿姨热情的和我道别。\r\n下车的一瞬间我回头看了一眼，只见那阿姨对着手机说：“儿子，
                \r\n刚才遇见一个姑娘特不错，可惜长得不好看，不然我肯定帮你要号码！”\r\n靠，阿姨你下车，我保证不打死你！",
                "hashId": "d4d750debbb73ced161066368348d611",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "小时候妈妈喂我饭之前会看书，我问她看的什么时。\r\n妈妈总是笑着告诉我：“是《育儿经验宝典》啊！”
                \r\n我很感动，直到我认识字才发现，妈妈看的是《猪崽饲养手册》。",
                "hashId": "d6161d9d7b113a920e7b33b25c3b5f0b",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "刚刚在舞蹈学校外接儿子，听到两个已经接到孩子到妈妈在聊天。
                \r\n妈妈甲：“你闺女这么小就是个美人胚子，大眼睛，双眼皮，瓜子脸。”\r\n妈妈乙：“是啊，长大了不知道要祸害多少男孩！”",
                "hashId": "6a6313c771b5bbc5b5688a926dcc836e",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "和室友说我约了一个女孩过夜，\r\n临出门室友提醒我：“要采取安全措施啊，保护好自己，你要没有我借你。”
                \r\n“不用不用，我自己有。”说完我马上打开抽屉，翻出一把刀带着出门了。",
                "hashId": "7d877e3ba86819a523175656e97b9cdf",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "“科学研究发现，睡眠不足会带来许多身心伤害：免疫力下降、\r\n记忆力减弱、易衰老、失去平衡等等，从而引发多种疾病。
                \r\n从科学角度讲，睡懒觉有助于身心健康。” \r\n“所以，李老师，这就是你在课堂上睡觉的原因？”校长生气的问我。",
                "hashId": "cb01359d7740e19435b9ea4e2d5516a1",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "做饭的时候发现没食用油了，\r\n就叫五岁的儿子“娃儿，去楼下小商店买壶油，顺便买点姜回来。别搞忘了。”
                \r\n儿子答应，边出门边念叨“油，姜，油，姜，油，姜，油…………”\r\n果然，回来带了瓶酱油……",
                "hashId": "473a3a81c621e03afadf453c23c989b5",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            },
            {
                "content": "我妈研究了几个新菜，邀请我品尝，\r\n结果我没有给她一个yes，被臭骂了一顿，\r\n要和我断绝关系。找我爸评理，
                \r\n老头说为了公平起见，我还是尝尝菜吧。\r\n吃完后，老头幽幽的说道，你和我也断绝关系吧。",
                "hashId": "8251a1ff78568624730f3d6ae8de7c6f",
                "unixtime": 1418814837,
                "updatetime": "2014-12-17 19:13:57"
            }
        ]
    }
}
"""
