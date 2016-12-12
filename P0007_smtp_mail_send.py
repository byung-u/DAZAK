#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = 'answer_test@gmail.com'
you = 'ask_test@gmail.com'

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link 이건 뭡니까"
msg['From'] = me
msg['To'] = you

answer = "Link는 연결입니다."
part1 = MIMEText(answer, 'plain', 'UTF-8')
msg.attach(part1)
print(msg.as_string())

s = smtplib.SMTP('localhost')
# s = smtplib.SMTP('localhost', 60011)
s.sendmail(me, you, msg.as_string())
print('send success')

s.quit()
