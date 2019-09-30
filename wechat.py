from wxpy import *

bot=Bot()
my_friend = bot.friends().search('孙玮聪', sex=MALE)[0]
my_friend.send(u"XXNet可以连接了给你发消息")
