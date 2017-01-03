#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def send_with_gmail(body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    gmail_user = 'my_id'  # 실제 google 로그인할 때 쓰는 ID
    gmail_pw = 'my_pw'    # 실제 google 로그인할 때 쓰는 Password

    from_addr = 'byeongwoo.jun@gmail.com'   # 보내는 사람 주소
    to_addr = 'iam.byungwoo@gmail.com'      # 받는 사람 주소

    msg=MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = 'Send email with Gmail'     # 제목
    msg.attach(MIMEText(body, 'plain', 'utf-8')) # 내용 인코딩
   
    ########################
    # https://www.google.com/settings/security/lesssecureapps
    # Make sure less_secure_apps select 'use'
    ########################
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pw)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print('successfully sent the mail')
    except BaseException as e:
        print("failed to send mail", str(e))

if __name__ == '__main__':
    send_msg = '''
    multi
    L
    I
    N
    E
    email
    send
    test.
    '''
    send_with_gmail(send_msg)
