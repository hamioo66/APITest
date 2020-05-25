import json
import time

import requests
from Crypto.Cipher import AES
import base64

"""
彩虹多多数据监控，监控专家预测方案

"""


class Aes_crypt:
    def __init__(self, key='d3YmI1BUOSE2S2YmalBVZUQ=', iv="0000000000000000"):
        # 加密key
        self.key = key
        # 加密矢量
        self.iv = iv
        self.mode = AES.MODE_CBC  # 模式
        self.BS = AES.block_size  # 长度16

        # ord（）函数就是用来返回单个字符的ascii值（0-255）或者unicode数值（）
        # 相反地，chr（）函数是输入一个整数【0，255】返回其对应的ascii符号
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode(
            'utf-8')  # 长度除16取余，16减余数缺多少，补多少个该数值的ascii码
        self.unpad = lambda s: s[0:-ord(s[-1])]  # 切掉后面的空格

    # 加密
    def en_crypt(self, text):
        text = text.encode('utf-8')
        text = self.pad(text)
        cryptor = AES.new(self.key.encode("utf-8"), self.mode, self.iv.encode("utf-8"))
        ciphertext = cryptor.encrypt(text)
        return base64.b64encode(ciphertext).decode('utf-8')

    # 解密
    def de_crypt(self, text):
        text = base64.b64decode(text.encode('utf-8'))
        cryptor = AES.new(self.key.encode("utf-8"), self.mode, self.iv.encode("utf-8"))
        plain_text = cryptor.decrypt(text).decode('utf-8')
        return self.unpad(plain_text)


if __name__ == '__main__':
    list_userid = {
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
    print(list_userid.keys())
    issuename = "2020012"
    url = "https://api.duoduoyoucai.com/jddods/recom/unct/public/handler"
    old_data = {
        39: {},
        5: {},
        6: {},
        63: {}
    }
    count = 0
    while True:
        for key in list_userid.keys():
            for userid in list_userid[key]:
                # print(userid)
                data = {"header": {"appVersion": "1.4.4", "idfa": "", "cmdName": "app_zz", "userId": "0",
                                   "uuid": "ffffffff-9f23-438e-922b-adc70033c587", "token": "", "cmdId": 10000,
                                   "platformVersion": "9", "action": "51009", "imei": "869940033602092",
                                   "userType": "0", "brand": "szcapp", "phoneName": "vivo", "platformCode": "Android"},
                        "body": {"issueName": issuename, "lotteryId": key, "recomTenantCode": "recom",
                                 "recomUserId": userid}}
                parames = json.dumps(data, sort_keys=True)
                aes = Aes_crypt()
                request = aes.en_crypt(parames)
                response = requests.post(url, data={"request": request}).json()
                print(response)
                num = len(response["data"]["schemeContentModelList"])
                member = {}
                for j in range(num):
                    if count == 0:
                        if response["data"]["schemeContentModelList"][j].get("numberList"):
                            member[response["data"]["schemeContentModelList"][j]["playtypeName"]] = \
                            response["data"]["schemeContentModelList"][j]["numberList"]
                        else:
                            member[response["data"]["schemeContentModelList"][j]["playtypeName"]] = \
                                response["data"]["schemeContentModelList"][j]["dwNumberList"]
                    else:
                        if response["data"]["schemeContentModelList"][j].get("numberList"):
                            if response["data"]["schemeContentModelList"][j]["numberList"] != old_data[key][userid][
                                response["data"]["schemeContentModelList"][j]["playtypeName"]]:
                                print("彩种id{}，用户id{}字段{}发生变化".format(key, userid,
                                                                     response["data"]["schemeContentModelList"][j][
                                                                         "playtypeName"]))
                                print("老数据：%s\r\n新数据：%s" % (
                                old_data[key][userid][response["data"]["schemeContentModelList"][j]["playtypeName"]],
                                response["data"]["schemeContentModelList"][j]["numberList"]))
                        else:
                            if response["data"]["schemeContentModelList"][j]["dwNumberList"] != old_data[key][userid][
                                response["data"]["schemeContentModelList"][j]["playtypeName"]]:
                                print("彩种id{}，用户id{}字段{}发生变化".format(key, userid,
                                                                     response["data"]["schemeContentModelList"][j][
                                                                         "playtypeName"]))
                                print("老数据：%s\r\n新数据：%s" % (
                                old_data[key][userid][response["data"]["schemeContentModelList"][j]["playtypeName"]],
                                response["data"]["schemeContentModelList"][j]["dwNumberList"]))

                if count == 0:
                    old_data[key][userid] = member
        count = 1
        time.sleep(300)
