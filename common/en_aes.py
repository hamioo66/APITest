# -*- coding:utf-8 -*-
'''
请求参数加密工具
python3  编码模式，报错,utf-8

'''
import time
from Crypto.Cipher import AES
import json
import base64


class Aes_crypt:
    def __init__(self, key='d3YmI1BUOSE2S2YmalBVZUQ=',iv="0000000000000000"):
        #加密key
        self.key = key
        #加密矢量
        self.iv = iv
        self.mode = AES.MODE_CBC  #模式
        self.BS = AES.block_size  #长度16

        #ord（）函数就是用来返回单个字符的ascii值（0-255）或者unicode数值（）
        #相反地，chr（）函数是输入一个整数【0，255】返回其对应的ascii符号
        self.pad = lambda s : s  +(self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode('utf-8')   #长度除16取余，16减余数缺多少，补多少个该数值的ascii码
        self.unpad = lambda s: s[0:-ord(s[-1])]  #切掉后面的空格

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
    obj = Aes_crypt()
    # c = {"header":{"appVersion":"8.1.7","idfa":"","cmdName":"app_zz","userID":"","uuid":"ffffffff-a218-c87e-8ce9-00650033c587","token":"","cmdID":"100000","platformVersion":"8.1.0","imei":"862204042998133","action":"8410","userType":1,"platformCode":"Android","phoneName":"OPPO"},"body":"{\"businessType\":1}"}
    d = {"header":{"appVersion":"8.1.7","idfa":"","cmdName":"app_zz","userID":"","uuid":"ffffffff-a218-c87e-8ce9-00650033c587","token":"","cmdID":"100000","platformVersion":"8.1.0","imei":"862204042998133","action":"8410","userType":1,"platformCode":"Android","phoneName":"OPPO"},"body":"{\"businessType\":1}"}
    # dict_to_json = json.dumps(d)
    # 测试加密
    d_enc = obj.en_crypt(json.dumps(d))
    print("加密:", type(d_enc))

    d_dec = obj.de_crypt(d_enc)
    print(type(d_dec))
    d_d = json.loads(d_dec)
    print(d_d)
