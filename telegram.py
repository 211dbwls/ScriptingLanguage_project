#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti

def replyAptData(date_param, user, loc_param):
    print(user, date_param, loc_param)
    res_list = noti.getData(loc_param, date_param)
    msg = ''
    for r in res_list:
        print(str(datetime.now()).split('.')[0], r)
        if len(r + msg) + 1 > noti.MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r + '\n'
        else:
            msg += r + '\n'
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, '%s 기간에 해당하는 데이터가 없습니다.' % date_param)


def save(user, loc_param):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    try:
        cursor.execute('INSERT INTO users(user, location) VALUES ("%s", "%s")' % (user, loc_param))
    except sqlite3.IntegrityError:
        noti.sendMessage(user, '이미 해당 정보가 저장되어 있습니다.')
        return
    else:
        noti.sendMessage(user, '저장되었습니다.')
        conn.commit()


def check(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
    cursor.execute('SELECT * from users WHERE user="%s"' % user)
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', location:' + data[1]
        noti.sendMessage(user, row)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('지역') and len(args) > 1:
        print('try to 지역', args[1])
        replyAptData('20200618', chat_id, args[1])
    elif text.startswith('저장') and len(args) > 1:
        print('try to 저장', args[1])
        save(chat_id, args[1])
    elif text.startswith('확인'):
        print('try to 확인')
        check(chat_id)
    else:
        noti.sendMessage(chat_id, """모르는 명령어입니다.\n지역 [지역번호] \n저장 [지역번호] \n확인 중 하나의 명령을 입력하세요.\n
            지역 ["서울특별시 6110000", "부산광역시 6260000", "대구광역시 6270000", "인천광역시 6280000", "광주광역시 629000", "세종특별자치시 5690000", "대전광역시 6300000", "울산광역시 6310000", 
            "경기도 6410000", "강원도 6420000", "충청북도 6430000", "충청남도 6440000", "전라북도 6450000", "전라남도 6460000", "경상북도 6470000", "경상남도 6480000", "제주특별자치도 6500000"] """)


today = date.today()
current_month = today.strftime('%Y%m')

print('[', today, ']received token :', noti.TOKEN)

bot = telepot.Bot(noti.TOKEN)
pprint(bot.getMe())

bot.message_loop(handle)

print('Listening...')

while 1:
    time.sleep(10)