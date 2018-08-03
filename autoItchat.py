#coding=utf-8
import itchat
import time
import random

itchat.auto_login(hotReload=True)

friends_list = itchat.get_friends(update=True)
name = itchat.search_friends(name=u'adolph')
XiaoMing = name[0]["UserName"]

message_list = [u'Hey,dude',u'Are you ok?',u'Bye~']
message_concent = random.sample(message_list,1)[0]

while True:
    itchat.send(message_concent,XiaoMing)
    time.sleep(5)

itchat.auto_logout()

