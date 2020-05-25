# -*- coding=utf-8 -*-
"""
@Destrible:首页appadmin配置
@Author:hamioo
@Time:2020/5/21 16:57
@File:api_002.py
"""
import requests
import json
from common.util_py3 import Prpcrypt
from common.getJsonKeyValue import GetKeyValue

url = 'https://api.duoduoyoucai.com/jddods/appadmin/unct/public/handler'
data = {"header": {"appVersion": "1.5.3", "idfa": "", "cmdName": "app_zz", "userId": "0",
                   "uuid": "00000000-5a0e-b2aa-0033-c5870033c587", "token": "", "cmdId": 10000, "platformVersion": "10",
                   "action": "1000", "userType": "0", "brand": "szcapp", "phoneName": "HUAWEI",
                   "platformCode": "Android"}, "body": "{}"}
Jdata = json.dumps(data, sort_keys=True)
request = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(Jdata)
response = requests.post(url, data={'request': request})
assert response.status_code
s = GetKeyValue(o=response.json(), mode='j')
b = GetKeyValue(o=data,mode='j')
# 轮播图
bannerList = s.search_key('bannerList')
# 中奖播报
bulletinList = s.search_key('bulletinList')
# 运营位
operationList = s.search_key('operationList')
# action
action = b.search_key('action')[0]
for i in range(len(operationList[0])):
    name = operationList[0][i]['name']
    actionName = operationList[0][i]['actionName']
    actionUrl = operationList[0][i]['actionUrl']
    print(f'首页两运营位配置了{name}{actionName}跳转链接是{actionUrl}')
#print(type(bannerList))
#print('首页配置了%d张轮播图,中奖播报有%d条'%(len(bannerList[0]),len(bulletinList[0])))
print(f'首页配置了{len(bannerList[0])}张轮播图,中奖播报有{len(bulletinList[0])}条')
print(f'接口action={action}')
