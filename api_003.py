# -*- coding=utf-8 -*-
"""
@Destrible:监控专家最新方案
@Author:hamioo
@Time:2020/5/22 11:41
@File:api_003.py
"""
import requests
import json
from common.util_py3 import Prpcrypt
from common.db import DB
from apscheduler.schedulers.blocking import BlockingScheduler
issuename = ''
url = 'https://api.duoduoyoucai.com/jddods/recom/unct/public/handler'
# 39 5 6 63 13 分别对应双色球、大乐透、福彩3d、排列3、七乐彩
user_id = {
    39: [803, 1870, 267, 867, 94, 1591, 663, 552, 36, 842, 1261, 372, 1140, 8, 563, 235, 1473, 1689, 99, 1046, 329,
         1775, 728, 959, 313, 1780, 51, 1134, 1911, 626, 1839, 306, 1495, 558, 537, 415, 164, 227, 273, 633, 159,
         73, 85, 343, 580, 830, 519, 64, 968, 215],
    5: [706, 305, 496, 932, 828, 561, 424, 606, 791, 522, 460, 817, 500, 1660, 1228, 1216, 746, 487, 1023, 737, 206,
        38, 442, 1524, 866, 997, 320, 1779, 1469, 567, 1817, 1172, 276, 666, 1699, 1950, 92, 1912, 242, 1639, 1588,
        1554, 603, 1538, 7, 1, 47, 115, 172, 79],
    6: [1241, 518, 1311, 568, 803, 677, 1731, 192, 251, 704, 1352, 1519, 1543, 631, 1688, 433, 295, 726, 866, 163,
        1467, 824, 1065, 1518, 1599, 1423, 1470, 1028, 1817, 1787, 645, 590, 775, 1946, 496, 1035, 898, 735, 1332,
        1440, 1154, 1476, 1223, 671, 572, 1905, 1622, 682, 1689, 1632
        ],
    63: [621, 594, 390, 1930, 1321, 1006, 1028, 1855, 894, 822, 950, 131, 1568, 35, 1179, 896, 1506, 98, 1362, 1105,
         511, 382, 1898, 1698, 602, 830, 840, 1408, 1013, 527, 1360, 1088, 1065, 1090, 1662, 1837, 667, 1412, 1381,
         1499, 961, 1281, 1974, 1534, 1670, 754, 1368, 216, 1031, 1758
         ]
}


def monitorExpert():
    lotteryIds = user_id.keys()
    for lotteryId in lotteryIds:
        for recomUserId in user_id[lotteryId]:
            data = {"header": {"appVersion": "1.5.3", "idfa": "", "cmdName": "app_zz", "userId": "0",
                               "uuid": "00000000-5a0e-b2aa-0033-c5870033c587", "token": "", "cmdId": 10000,
                               "platformVersion": "10",
                               "action": "51009", "userType": "0", "brand": "szcapp", "phoneName": "HUAWEI",
                               "platformCode": "Android"},
                    "body": {"issueName": issuename, "lotteryId": lotteryId, "recomTenantCode": "recom",
                             "recomUserId": recomUserId}}
            request = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(json.dumps(data, sort_keys=True))
            count = 0
            old_data = []
            response = requests.post(url, data={'request': request}).json()
            #print(response, recomUserId)
            if response['msg'] == '操作成功！':
                lotteryName = response["data"]['lotteryName']
                ls = response["data"]["schemeContentModelList"]
                for i in range(len(ls)):
                    issueName = ls[i]['issueName']
                    playtypeId = ls[i]['playtypeId']
                    playtypeName = ls[i]['playtypeName']
                    if 'dwNumberList' not in ls[i]:
                        numberList = ls[i]['numberList']
                    else:
                        numberList = ls[i]['dwNumberList']



                    if count == 0:
                        old_data = old_data+[recomUserId, issueName, lotteryName, playtypeId, playtypeName, numberList]
                        #print(old_data)
                        # sql = 'INSERT INTO expert_schedule(lotteryId,lotteryName,recomUserId,issueName,playtypeId,playtypeName,numberList) VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(
                        #     lotteryId, lotteryName, recomUserId, issueName, playtypeId, playtypeName, numberList)
                        # a = DB()
                        # a.executesql(sql)
                    else:
                        new_data = [recomUserId, issueName, lotteryName, playtypeId, playtypeName, numberList]
                        dif = [x for x in [old_data+new_data] if x not in old_data]
                        print(f'专家{recomUserId}{lotteryName}{playtypeName}：{dif}的数据变了')
                count = count + 1
            else:
                print(f'当前专家{recomUserId}没有最新推荐')
            #print(f"循环了{count}次")


if __name__ == "__main__":
    sched = BlockingScheduler()
    sched.add_job(monitorExpert,'interval', hours=0.1, start_date='2020-5-26 00:00:00', end_date='2020-06-15 23:59:59')
    sched.start()
