#!/usr/bin/python2.7
# coding-utf-8

import itchat
import time


itchat.auto_login(hotReload=True)

while True:
	itchat.send_msg(msg='changyu', toUserName=u'@a619a9480b976ce7c57bd4dc65372ea3')
	time.sleep(1)

itchat.logout()




