# -*- coding=utf-8 -*-
import json
"""
json中递归查找需要的key的value
"""
import json

class GetKeyValue(object):
    def __init__(self, o, mode='j'):
        self.json_object = None
        if mode == 'j':
            self.json_object = o
        elif mode == 's':
            self.json_object = json.loads(o)
        else:
            raise Exception('Unexpected mode argument.Choose "j" or "s".')

        self.result_list = []

    def search_key(self, key):
        self.result_list = []
        self.__search(self.json_object, key)
        return self.result_list

    def __search(self, json_object, key):

        for k in json_object:
            if k == key:
                self.result_list.append(json_object[k])
            if isinstance(json_object[k], dict):
                self.__search(json_object[k], key)
            if isinstance(json_object[k], list):
                for item in json_object[k]:
                    if isinstance(item, dict):
                        self.__search(item, key)
        return
gkv = GetKeyValue(o={'code': 0, 'currentTimeMillis': 1589869654722, 'data': {'issueName': '2020012', 'lotteryId': 39, 'lotteryName': '大乐透', 'operationList': [{'actionId': 1000, 'actionParams': '', 'actionUrl': 'https://engine.tuirabbit.com/index/activity?appKey=4FiHCzHJPbvqUPThtSXkJBQvHSxt&adslotId=342241', 'imgUrl': 'https://fdfs.jdd.com/group1/M00/2C/BB/rBACDl65QMCAUtDWAADdicIJjaA696.jpg', 'name': '易有料广告'}], 'schemeContentModelList': [{'issueName': '2020012', 'numberList': [28], 'numberType': 1, 'playtypeId': 1001, 'playtypeName': '红球独胆'}, {'issueName': '2020012', 'numberList': [12, 28], 'numberType': 1, 'playtypeId': 1002, 'playtypeName': '红球双胆'}, {'issueName': '2020012', 'numberList': [12, 18, 28], 'numberType': 1, 'playtypeId': 1003, 'playtypeName': '红球三胆'}, {'issueName': '2020012', 'numberList': [2, 3, 10, 12, 18, 27, 28, 29, 31, 33], 'numberType': 1, 'playtypeId': 1010, 'playtypeName': '红球10码'}, {'issueName': '2020012', 'numberList': [2, 3, 9, 10, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, 25, 27, 28, 29, 31, 33], 'numberType': 1, 'playtypeId': 1020, 'playtypeName': '红球20码'}, {'issueName': '2020012', 'numberList': [2, 3, 4, 5, 6, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 27, 28, 29, 31, 33, 34], 'numberType': 1, 'playtypeId': 1025, 'playtypeName': '红球25码'}, {'issueName': '2020012', 'numberList': [8, 24, 35], 'numberType': 1, 'playtypeId': 1103, 'playtypeName': '红球杀三'}, {'issueName': '2020012', 'numberList': [8, 22, 24, 26, 30, 35], 'numberType': 1, 'playtypeId': 1106, 'playtypeName': '红球杀六'}, {'issueName': '2020012', 'numberList': [12], 'numberType': 2, 'playtypeId': 2001, 'playtypeName': '蓝球定一'}, {'issueName': '2020012', 'numberList': [2, 12], 'numberType': 2, 'playtypeId': 2002, 'playtypeName': '蓝球定二'}, {'issueName': '2020012', 'numberList': [1, 2, 4, 5, 8, 12], 'numberType': 2, 'playtypeId': 2006, 'playtypeName': '蓝球定六'}, {'issueName': '2020012', 'numberList': [3, 6, 11], 'numberType': 2, 'playtypeId': 2103, 'playtypeName': '蓝球杀三'}], 'schemeId': 2027101}, 'msg': '操作成功！', 'stamp': 0}, mode='j') # mode=j意味传入的object是一个json对象
#gkv = GetKeyValue(o={'demo': 'show demo'}, mode='j')
print(gkv.search_key('numberList'))

