#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    nums = [2, 21, 13, 444, 59, 67, 7, 18, 909, 1004, 2, 21]

    dict_test = {}
    for i, num in enumerate(nums):
        cnt = dict_test.get(num)
        if cnt is None:
            cnt = 0
        dict_test[num] = cnt + 1

    print(dict_test)
