#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import configparser

config = configparser.ConfigParser()
config.readfp(open('conf.ini'))
url = config.get('0001', 'url')

client = requests.session()
client.get(url)

post_data = {
    'email': 'test@maaaaail.com',
    'csrfmiddlewaretoken': client.cookies['csrftoken']
    }
r = client.post(url, data=post_data, headers=dict(Referer=url))
print(r)
