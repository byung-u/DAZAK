#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import telepot

from requests import get
from bs4 import BeautifulSoup

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CURRENT_REPO = 10

def send_telegram():
    config = configparser.ConfigParser()
    config.readfp(open('conf.ini'))
    telegram_token = config.get('0002', 'telegram_token')
    chat_id = config.get('0002', 'chat_id')
    bot = telepot.Bot(telegram_token)
    bot.sendMessage(chat_id, "Repository Add Check it pyconkr!!")


def send_email():
    me = 'test@notify.com'
    you = 'mymail@gmail.com'

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "pyconkr 리포지터리가 바꼈다."
    msg['From'] = me
    msg['To'] = you

    answer = "가서 시작했나 확인하고 contribution 가능한지 찔러보삼"
    part1 = MIMEText(answer, 'plain', 'UTF-8')
    msg.attach(part1)
    #print(msg.as_string())
    #print('send success')

    s = smtplib.SMTP('localhost')
    s.sendmail(me, you, msg.as_string())
    s.quit()



if __name__ == '__main__':

    url = "https://github.com/pythonkr"
    r = get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    cnt = 0
    for link in  soup.find_all('a'):
        repo = link.get('href')
        repo = str(repo)
        if (repo.startswith('/pythonkr')) and (repo.count('/') == 2):
            #print(repo)
            cnt+=1

    if (cnt < CURRENT_REPO):
        send_telegram()
        send_email()

    sys.exit(0)
