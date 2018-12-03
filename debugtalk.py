#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import time

# 获取cookie（sessionid）
def get_cookie():
    url = 'http://10.53.27.229:8000/api/login/'
    headers = {
        "X-Requested-With": "XMLHttpRequest"
    }
    data = {
        "account": "wangmeng",
        "password": "admin123456"
    }
    res = requests.post(url=url, data=data, headers=headers)
    print(res.headers.get('Set-Cookie'))
    print(res.headers.get('Set-Cookie').split(';')[0])
    cookie = res.headers.get('Set-Cookie').split(';')[0]
    return cookie

# 设置时间
def my_time():
    s = 20
    return s

# hook机制等待
def hook_sleep():
    time.sleep(my_time())
