#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

# good reference: https://pymotw.com/2/re/
import re

# 00:36:47.450 --> 00:36:50.560
test_str = '00:36:47.450 --> 00:36:50.560'
p = re.compile(r'\d+\d+:\d+\d+:\d+\d+\.\d+\d+\d+\ \-\-\>\ \d+\d+:\d+\d+:\d+\d+\.\d+\d+\d+')
m = p.match(test_str)
if m is not None:  
    print('[ OK]got it: ', test_str)
else:
    print('[NOK]not matched: ', test_str)

# 'http://$NUMBER or STRING.tistory.com/$NUMBER'
# 'http://jisikshare.tistory.com/24'
test_arr = ('http://jisikshare.tistory.com/24',
        'http://132423.tistory.com/243423',
        'http://132423.tistory.com/abcdse',
        'http://jisikshare.tistory.com/243423',
        'http://asdf.asdfasdf.tistory.com/243423',
        'http://kkkwer.tistory.com/243',
        )
p = re.compile(r'^http://(\w+).tistory.com/(\d+)')
for i in range(len(test_arr)):
    m = p.match(test_arr[i])
    if m is not None:  
        print('[ OK]got it: ', test_arr[i])
    else:
        print('[NOK]not matched: ', test_arr[i])
