#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# 주의사항
# Google sheet 권한 설정이 안 된 경우에 동작 안하므로
# 권한 설정 반드시 확인

import httplib2

import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

import smtplib
from email.mime.text import MIMEText

import configparser

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

config = configparser.ConfigParser()
config.readfp(open('conf.ini'))
CLIENT_SECRET_FILE = config.get('0006', 'CLIENT_SECRET_FILE')

APPLICATION_NAME = 'support'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_file_name = config.get('0006', 'credential_file_name')
    credential_path = os.path.join(credential_dir, credential_file_name)

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)

    # https://developers.google.com/sheets/guides/concepts
    spreadsheetId = config.get('0006', 'spreadsheetId')
    rangeName = 'recv_mail!A2:G'
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            print('%s %s' % (row[1], row[6]))
            answer = str(row[6])
            msg = MIMEText(answer.encode('utf-8'), _charset='utf-8')
            msg['Subject'] = 'Re:%s', (row[2])
            msg['From'] = 'support@test.kr'
            msg['To'] = row[1]

            s = smtplib.SMTP('localhost')
            # s = smtplib.SMTP('localhost', 60011)
            s.sendmail('support@test.kr', [row[1]], msg.as_string())
            s.quit()


if __name__ == '__main__':
    main()
