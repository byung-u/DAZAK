#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-
import re

test_str = '00:36:47.450 --> 00:36:50.560'
p = re.compile(r'\d+\d+:\d+\d+:\d+\d+\.\d+\d+\d+\ \-\-\>\ \d+\d+:\d+\d+:\d+\d+\.\d+\d+\d+')
m = p.match(test_str)
if m is not None:  # 00:36:47.450 --> 00:36:50.560
    print('got it: ', test_str)
