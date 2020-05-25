# -*- coding=utf-8 -*-
"""
@Destrible:首页资讯接口
@Author:hamioo
@Time:2020/5/21 16:57
@File:api_002.py
"""
import requests
from common.util_py3 import Prpcrypt
import json
import xlrd
from common.getJsonKeyValue import GetKeyValue

# 读取数据文件
workbook = xlrd.open_workbook('params/news.xlsx')
# 查看excel文件中的sheet个数以及sheet名称
sheet_num = workbook.nsheets
names = workbook.sheet_names()
# print(sheet_num, names)
news = workbook.sheet_by_name('Sheet1')
# 读取工作表的行数和列数
news_rows = news.nrows
news_cols = news.ncols
url = 'https://api.duoduoyoucai.com/carina/unct/public/handler'
for i in range(1, news_rows):
    # print(i)
    channelId = int(news.cell(i, 0).value)
    lotteryId = int(news.cell(i, 1).value)
    loteryName = news.cell(i, 2).value

    print(
        f'--------------------------------------{loteryName}的资讯，其channelId是{channelId}，lotteryId是{lotteryId}----------------------------------------')
    data = {"header": {"appVersion": "1.5.3", "idfa": "", "cmdName": "app_zz", "userId": "0",
                       "uuid": "00000000-5a0e-b2aa-0033-c5870033c587", "token": "", "cmdId": 10000,
                       "platformVersion": "10", "action": "1009", "userType": "0", "brand": "szcapp",
                       "phoneName": "HUAWEI", "platformCode": "Android"},
            "body": {"channelId": channelId, "lotteryId": lotteryId, "size": 15, "timeStamp": ""}}
    # action
    s = GetKeyValue(o=data, mode='j')
    actionName = s.search_key('action')[0]
    newsList = s.search_key('newsList')
    print(f'接口action={actionName}\n')
    if len(newsList) == 0:
        print('资讯返回数据为空')
    Jdata = json.dumps(data)
    request = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(Jdata)
    response = requests.post(url, data={'request': request})
    if response.status_code == 200:
        print(f'接口请求成功，返回json为:{response.json()}\n')
        print(f'响应时间为{response.elapsed.total_seconds()}\n')
