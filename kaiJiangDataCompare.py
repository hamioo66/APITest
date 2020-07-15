# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/6/30 14:35
@File:kaiJiangDataCompare.py
"""
from common.util_py3 import Prpcrypt
import requests
import json
import difflib
import time
import sys


# f = open('logs/a.log', 'a')
# sys.stdout = f

def comp_result(urlOn, urlTest, file):
    with open(file, 'r', encoding='utf-8') as w:
        lines = w.readlines()
        for line in lines:
            regionId = line.split('，')[0]
            regionName = line.split('，')[1].split('\n')[0]
            data = {"header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz",
                               "userType": 1,
                               "uuid": "df734215c430467f913c3d3fff579f5e", "userID": "", "platformCode": "h5mobile",
                               "token": ""},
                    "body": {"regionId": regionId}}
            request = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(json.dumps(data))
            responseOn = requests.post(urlOn, data={'request': request}, verify=False)
            responseTest = requests.post(urlTest, data={'request': request}, verify=False)
            on = json.dumps(responseOn.json(), sort_keys=True, ensure_ascii=False, indent=4)
            test = json.dumps(responseTest.json(), sort_keys=True, ensure_ascii=False, indent=4)
            diff = difflib.context_diff(on.splitlines(keepends=True), test.splitlines(keepends=True), '线上', '测试')
            print(f'\n************************当前彩种{regionName}************************\n' + ''.join(diff), end="")


def comp_common(urlOn, urlTest, data, *args):
    request = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(json.dumps(data))
    print(request)
    responseOn = requests.post(urlOn, data={'request': request}, verify=False)
    responseTest = requests.post(urlTest, data={'request': request}, verify=False)
    onJ = responseOn.json()
    testJ = responseTest.json()
    del onJ['msg']
    del onJ['stamp']
    on = json.dumps(onJ, sort_keys=True, ensure_ascii=False, indent=4)
    del testJ['msg']
    del testJ['stamp']
    test = json.dumps(testJ, sort_keys=True, ensure_ascii=False, indent=4)
    diff = difflib.context_diff(on.splitlines(keepends=True), test.splitlines(keepends=True), '线上', '测试')
    print(urlOn, urlTest)
    print(''.join(diff), end="")


if __name__ == "__main__":
    """
    result 正常
    """
    file = 'file/regionId.txt'
    # comp_result('http://lottery.jdddata.com/result', 'http://114.118.2.15/result', file)

    """
    region 正常
    """
    region_data = {
        "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz", "userType": 1,
                   "uuid": "8bf124368b624592860603a163922a79", "userID": "", "platformCode": "h5mobile", "token": ""},
        "body": {"lotteryType": "2"}}
    # comp_common(urlOn='http://lottery.jdddata.com/region', urlTest='http://114.118.2.15/region', data=region_data)
    """
    locate
    """
    # locate_data = {
    #     "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz", "userType": 1,
    #                "uuid": "232d7ed66d824d0daa6cbbf56f83d538", "userID": "", "platformCode": "h5mobile", "token": ""},
    #     "body": "{\"lotteryType\":\"1\"}"}
    # comp_common('http://lottery.jdddata.com/result/locate', 'http://114.118.2.15/result/locate', data=locate_data)  #result/locate
    # with open(file, 'r', encoding='utf-8') as w:
    #     lines = w.readlines()
    #     for line in lines:
    #         regionId = line.split('，')[0]
    #         regionName = line.split('，')[1].split('\n')[0]
    #         result_1 = {
    #             "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz", "userType": 1,
    #                        "uuid": "232d7ed66d824d0daa6cbbf56f83d538", "userID": "", "platformCode": "h5mobile", "token": ""},
    #             "body": {"regionId": regionId, "lotteryType": "2", "lotteryBelong": " "}}
    #         print(f'\n*********************{regionName}*********************\n')
    #         comp_common('http://lottery.jdddata.com/result/1', 'http://114.118.2.15/result/1', data=result_1)   #result/1

    catagory_default = {"header": {"appVersion": "1.0.0", "idfa": "", "cmdName": "app_zz", "userID": "MTY=",
                                   "uuid": "ffffffff-d5f8-bf85-1f91-171a0033c587", "token": "VHlwZSI6M", "cmdID": "0",
                                   "platformVersion": "5.1.1", "action": "110", "imei": "865800028773239",
                                   "userType": "1", "platformCode": "Android", "phoneName": "ONEPLUS"}, "body": {}}
    # with open('file/all.txt', 'r', encoding='utf-8') as w:
    #     lines = w.readlines()
    #     for line in lines:
    #         lotteryName = line.split(':')[0]
    #         lotteryId = line.split(':')[1].split('\n')[0]
    #         result_more = {"header": {"appVersion": "1.0.0", "idfa": "", "cmdName": "app_zz", "userID": "MTY=",
    #                                        "uuid": "ffffffff-d5f8-bf85-1f91-171a0033c587", "token": "VHlwZSI6M", "cmdID": "0",
    #                                        "platformVersion": "5.1.1", "action": "110", "imei": "865800028773239",
    #                                        "userType": "1", "platformCode": "Android", "phoneName": "ONEPLUS"}, "body": {"lotteryId":lotteryId,"issueNum":"50"}}
    #         print(f'\n*********************当前彩种{lotteryName}*********************\n')
    #         comp_common('http://lottery.jdddata.com/result/more', 'http://114.118.2.15/result/more',data=result_more)  # /result/more
    index_2 = {"header": {"appVersion": "1.0.0", "idfa": "", "cmdName": "app_zz", "userID": "MTY=",
                                   "uuid": "ffffffff-d5f8-bf85-1f91-171a0033c587", "token": "VHlwZSI6M", "cmdID": "0",
                                   "platformVersion": "5.1.1", "action": "110", "imei": "865800028773239",
                                   "userType": "1", "platformCode": "Android", "phoneName": "ONEPLUS"}, "body": {"pCode":"job"}}

    """
    resultall
    # """
    # comp_common('http://lottery.jdddata.com/result/all', 'http://114.118.2.15/result/all', data=locate_data)  #result/all

    # comp_common('http://lottery.jdddata.com/category/default', 'http://114.118.2.15/category/default', data=catagory_default) #category/default
    # comp_common('http://lottery.jdddata.com/category/time', 'http://114.118.2.15/category/time', data=catagory_default)  #category/time
    # comp_common('http://lottery.jdddata.com/index/2', 'http://114.118.2.15/index/2', data=index_2)# index/2

    # with open('file/all.txt', 'r', encoding='utf-8') as w:
    #     lines = w.readlines()
    #     for line in lines:
    #         lotteryName = line.split(':')[0]
    #         lotteryId = line.split(':')[1].split('\n')[0]
    #         trend_miss = {"header": {"appVersion": "1.0.0", "idfa": "", "cmdName": "app_zz", "userID": "MTY=",
    #                                  "uuid": "ffffffff-d5f8-bf85-1f91-171a0033c587", "token": "VHlwZSI6M",
    #                                  "cmdID": "0",
    #                                  "platformVersion": "5.1.1", "action": "110", "imei": "865800028773239",
    #                                  "userType": "1", "platformCode": "Android", "phoneName": "ONEPLUS"},
    #                       "body": {"lotteryId": lotteryId, "type": "6"}}
    #         print(f'\n*********************当前彩种{lotteryName}*********************\n')
    #         comp_common('http://lottery.jdddata.com/trend/miss', 'http://114.118.2.15/trend/miss',data=trend_miss)  # trend/miss
    """
    rencentDay
    """
    # with open('file/highLotteryName.txt', 'r', encoding='utf-8') as w:
    #     lines = w.readlines()
    #     for line in lines:
    #         lotteryName = line.split(':')[0]
    #         lotteryId = line.split(':')[1].split('\n')[0]
    #         rencentDay_data = {
    #             "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz", "userType": 1,
    #                        "uuid": "89c0026e34994888b39a69ce40663925", "userID": "", "platformCode": "h5mobile",
    #                        "token": ""}, "body": {"lotteryId": lotteryId, "num": 30}}
    #
    #         print(f'\n*********************当前彩种{lotteryName}*********************\n')
    #         comp_common(urlOn='http://lottery.jdddata.com/issue/recentDay', urlTest='http://114.118.2.15/issue/recentDay',
    #                     data=rencentDay_data)
    # w.close()

    """
    day
    """
    # with open('file/highLotteryName.txt', 'r', encoding='utf-8') as w:
    #     lines = w.readlines()
    #     for line in lines:
    #         lotteryName = line.split(':')[0]
    #         lotteryId = line.split(':')[1].split('\n')[0]
    #         day_data = {
    #             "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz",
    #                        "userType": 1,
    #                        "uuid": "e6d70af36af5445bb06a33dd0ad25892", "userID": "", "platformCode": "h5mobile",
    #                        "token": ""},
    #             "body": {"lotteryId": lotteryId, "issueDay": "2020-06-30"}}
    #         print(f'\n*********************当前彩种{lotteryName}*********************\n')
    #         comp_common(urlOn='http://lottery.jdddata.com/result/day',urlTest='http://114.118.2.15/result/day',data=day_data)

    # """
    # detail
    # """
    #
    # with open('file/nationLotteryName.txt', 'r', encoding='utf-8') as w:
    #     lines = w.readlines()
    #     for line in lines:
    #         lotteryName = line.split(':')[0]
    #         lotteryId = line.split(':')[1].split('\n')[0]
    #         detail_data = {
    #             "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz",
    #                        "userType": 1,
    #                        "uuid": "08372c2631cc4daf89374a44b8e19f2b", "userID": "", "platformCode": "h5mobile",
    #                        "token": ""},
    #             "body": {"lotteryId": lotteryId, "issueNo": "20063027"}}
    #         print(f'\n*********************当前彩种{lotteryName}*********************\n')
    #         comp_common(urlOn='http://lottery.jdddata.com/detail', urlTest='http://114.118.2.15/detail', data=detail_data)

    # rencentNo_data = {
    #     "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz",
    #                "userType": 1,
    #                "uuid": "56e777d4f40d4bf3ab5ed84ce545e69f", "userID": "", "platformCode": "h5mobile",
    #                "token": ""},
    #     "body": {"lotteryId": '2013', "issueNum": 10}}
    # print(f'\n*********************当前彩种{lotteryName}*********************\n')
    # comp_common(urlOn='https://lottery.jdddata.com/issue/recentNo', urlTest='https://114.118.2.15/issue/recentNo',
    #                         data=rencentNo_data)

    """
    走势图
    """
    with open('file/all.txt', 'r', encoding='utf-8') as w:
        lines = w.readlines()
        for line in lines:
            lotteryName = line.split(':')[0]
            lotteryId = line.split(':')[1].split('\n')[0]
            trend_data = {
                "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "cmdName": "h5_zz", "agencyId": "",
                           "userType": 1, "uuid": "aea6fcfe86504a558549aa67b3fa743b", "userID": "", "platformCode": "h5mobile",
                           "token": ""}, "body": {"lotteryId":'2041'}}
            #print(f'\n*********************当前彩种{lotteryName}*********************\n')
            # comp_common(urlOn='http://lottery.jdddata.com/trend/common', urlTest='http://114.118.2.15/trend/common',
            #                         data=trend_data)
            comp_common(urlOn='http://lottery.jdddata.com/trend', urlTest='http://114.118.2.15/trend',
                        data=trend_data)
            time.sleep(10)

