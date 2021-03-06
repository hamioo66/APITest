# -*- coding:utf-8 -*-
'''
请求参数加密工具
python3  编码模式，报错,utf-8

'''
import time
from Crypto.Cipher import AES
import json
import base64


class Prpcrypt:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC
        self.BS = AES.block_size

        #位数不够，补位AES 长度128（16位字节数）
        self.pad = lambda s: s + (self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS).encode('utf-8')
        self.unpad = lambda s: s[0:-ord(s[-1])]

    # 加密
    def encrypt(self, text):
        text = text.encode('utf-8')
        text = self.pad(text)
        cryptor = AES.new(self.key.encode("utf-8"), self.mode,self.iv.encode("utf-8"))
        ciphertext = cryptor.encrypt(text)

        return str(base64.b64encode(ciphertext),encoding='utf-8')

    # 解密
    def decrypt(self, text):
        text = text.encode('utf-8')
        cryptor = AES.new(self.key.encode('utf-8'), self.mode,self.iv.encode('utf-8'))
        plain_text = str(cryptor.decrypt(base64.b64decode(text)),encoding='utf-8')
        return self.unpad(plain_text.rstrip('\0'))

if __name__ == '__main__':
    # 测试加密

    d = {"header":{"appVersion":"4.0.2","cmdId":0,"platformVersion":"4.0.2","cmdName":"h5_zz","userType":1,"uuid":"09dd7e786dbf46078d8adbb2cbe08827","userID":"","platformCode":"h5mobile","token":""},"body":{"lotteryId":"1000","issueNo":"18055"}}

    a = '2Rc75HULvIxtcnOZfmdp8Y5aukl3fPSYuH2SnsEMW9DmbnlZLapwgJEYpxC6IllEtxTPINfcI67YTJGmd9NIUko4/f3qYisTbH6r7TTMnMeR4imxPj6tGolk/QAwunbtiHi4/10gNYlryHzThV0enmIobM5KjZ/ELiazNwitSTnGwkiGMe4OAVbggXiZ8zBTro8Ue591HpE1Rw+aOhgkdczk0enDkmtrsOTt/33Q6SJmhQoXdSWH0P5aqz/v8ThjWgFNWq8zo8twjKeTwfdPzc7ULlJLYixBT+MfLD64zpmwloNFxiKztO1qdJvs6YJNhXM36mfy1SWbPYVw+qWjk55exvFIOwdzqK1nj578tNGFiMIY8ycu7xuVspZ4NFpT9pHw4Lrw5s9ASJ9XpBPkWz/OGtXZ5Y0wMwHhx2FTTX8='

    dict_to_json = json.dumps(d)

    d_new = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").encrypt(dict_to_json)

    a_new = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', "0000000000000000").decrypt(a)




    print("加密:", d_new)
    print("解密:", a_new)
