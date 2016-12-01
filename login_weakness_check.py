#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import requests
from urllib.parse import urlencode

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

url = 'http://ec2-52-78-210-20.ap-northeast-2.compute.amazonaws.com:10051/login/'

def main():
    client = requests.session()
    client.get(url)
    csrftoken = client.cookies['csrftoken']
    for i in range(1, 10):
        email = 'jjjjjjjjjjjjjjjjjjjjjjj@jjjjjj.jjjj%s' % i

        post_data = {
            'id': '18',
            'email': email,
            'token': 'asdafalskfajslfksjdfsdfdads',
            'created': '2016-11-29 07:19:05.339450',
            'csrfmiddlewaretoken': csrftoken
            }
        r = client.post(url, data=post_data, headers=dict(Referer=url))
        print(r)

if __name__ == '__main__':
    main()
    sys.exit(1)
