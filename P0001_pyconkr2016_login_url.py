#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests

url = 'http://ec2-52-78-210-2f.ap-northeast-2.compute.amazonaws.com:10051/login/'
client = requests.session()
client.get(url)

post_data = {
    'email': 'test@maaaaail.com',
    'csrfmiddlewaretoken': client.cookies['csrftoken']
    }
r = client.post(url, data=post_data, headers=dict(Referer=url))
print(r)
