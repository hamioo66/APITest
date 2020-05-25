# -*- coding:utf-8 -*-
import requests
from common.util_py3 import Prpcrypt
import json

url = "https://data2c.jdddata.com/number/info/list/v1"
parms = {"header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 1009, "cmdName": "h5_zz",
                    "uuid": "223b261716f84bc19d3b005ed22b834e", "brand": "szcapp", "platformCode": "h5mobile"},
         "body": {"timeStamp": "", "size": 10, "labels": "2|3|4|5|6|7|8"}}
newParms = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(json.dumps(parms))


def get_response(url, data=None, json=None):
    response = requests.post(url, data=data, json=json)
    return response


def parms_to(self, page, size, timestamp, batchNumber):
    self.page = page
    self.size = size
    self.timestamp = timestamp
    self.batchNumber = batchNumber
    if page != 1:
        parms['body']['page'] = str(page)
        parms['body']['size'] = size
        parms['body']['timestamp'] = timestamp
        parms['body']['batchNumber'] = batchNumber
    else:
        parms['body']['page'] = str(1)
    datas = get_response(url, data={'request': newParms})
    newdatas = datas.json()
    request_time = datas.elapsed.total_seconds()


def page_to():
    pass


if __name__ == "__main__":
    parms_to('1','2','15','','')
    #parms_to(2,10,)
    # datas = get_response(url, data={'request': newParms})
    # print(datas.json())
    # newdatas = datas.json()
    # print(newdatas['data'][0]['title'])
