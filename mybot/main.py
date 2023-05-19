from pycqBot.data import Message
from pycqBot.cqApi import cqHttpApi, cqLog
import logging
from pycqBot.data import *
from logging import INFO
from pycqBot.cqCode import image
import total_price, missing, mini_price_get

# bot基础设置
cqLog(logging.INFO)
cqapi = cqHttpApi()
csgo_bot = cqapi.create_bot(options={'commandSign': ''
                                     }
                            , group_id_list=[
        # 725665163,257506703
        # 替换为你的QQ群号，第一个是csgo友友，第二个是测试
    ],
                            )


# 获取总趋势的指令
def all_sell_command(commandData, message: Message):
    result = total_price.all_sell_data()
    message.reply("%s\n---------------------\n以上数据来自于CSGOOB网站" % (result))


csgo_bot.command(all_sell_command, "趋势", {
    "help": [
        "趋势 - 显示现在的数据总趋势"
    ],
    "type": "all"})


# 获取黄金网的指令
def get_huangjinwang(commandData, message: Message):
    result = mini_price_get.get_data_hjw()
    message.reply("%s" % result)


csgo_bot.command(get_huangjinwang, "黄金网", {
    "help": [
        "黄金网 - 显示现在该饰品在buff的价格"
    ],
    "type": "all"})


# 获取石鳞的指令
def get_sl(commandData, message: Message):
    result = mini_price_get.get_data_sl()
    message.reply("%s" % result)


csgo_bot.command(get_sl, "石鳞", {
    "help": [
        "石鳞 - 显示现在该饰品在buff的价格"
    ],
    "type": "all"})


# 获取战痕累累的指令
def get_zhanhen(commandData, message: Message):
    result = mini_price_get.get_data_zhanhen()
    message.reply("%s" % result)


csgo_bot.command(get_zhanhen, "战痕累累", {
    "help": [
        "战痕累累 - 显示现在该饰品在buff的价格"
    ],
    "type": "all"})


# usp yinhuaji
def get_uspyhj(commandData, message: Message):
    result = mini_price_get.get_data_uspyhj()
    message.reply("%s" % result)


csgo_bot.command(get_uspyhj, "usp印花集", {
    "help": [
        "usp印花集 - 显示现在该饰品在buff的价格"
    ],
    "type": "all"})


# a1 yinhuaji
def get_a1yhj(commandData, message: Message):
    result = mini_price_get.get_data_a1yhj()
    message.reply("%s" % result)


csgo_bot.command(get_a1yhj, "a1印花集", {
    "help": [
        "a1印花集 - 显示现在该饰品在buff的价格"
    ],
    "type": "all"})


# 获取作者赞赏码
def priv(commandData, message: Message):
    # image("图片名", "图片url")
    message.reply("作者已经很久没吃饭了 %s" % image("a",
                                                    'https://usercontent.githubfast.com/user-images/129657153/237091352-9b865185-e6ed-4494-9824-a1761a82e30c.JPG'
                                                    ))


csgo_bot.command(priv, "打赏",
                 {"help": ["打赏 - 打赏一下作者吧"],
                  "type": "all"})


# 没有用的小程序

def miss(commandData, message: Message):
    message.reply("想念的第%s天" % missing.result)


csgo_bot.command(miss, "想念", {"type": "all"})


def a6(commandData, message: Message):
    message.reply("6什么6%s" % image('a', 'https://www.emojidaquan.com/Pics/meme/202301/8bbe0c4564f2.jpg'))


csgo_bot.command(a6, "6", {"type": "all"})


def as6(commandData, message: Message):
    message.reply("6什么6%s" % image('a', 'https://www.emojidaquan.com/Pics/meme/202301/8bbe0c4564f2.jpg'))


csgo_bot.command(as6, "666", {"type": "all"})
# 开启bot
csgo_bot.start()
