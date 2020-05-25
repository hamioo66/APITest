# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/11/22
describle:
"""
import requests
params = {"KEY":"VALUE"}
r= requests.get('https://www.baidu.com', params=params)
print(r.status_code)

print(r.text)
print(r.encoding) # 编码
print(r.content) # 获取返回内容（自动编码gzip）
