#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

url = 'http://ec2-52-78-210-20.ap-northeast-2.compute.amazonaws.com:10051/login/'

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
