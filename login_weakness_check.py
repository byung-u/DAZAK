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
        'email': email,
        'csrfmiddlewaretoken': csrftoken
    }
    r = client.post(url, data=post_data, headers=dict(Referer=url))
    print(r)
