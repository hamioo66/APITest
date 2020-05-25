import base64
import json
import random
import re
import time

import pymysql
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.en_aes import Aes_crypt


# 生成手机号
def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7][random.randint(0, 1)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(10000000, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


#   加密请求
def en_post(url, data, bc=None):
    aes = Aes_crypt()
    data = aes.en_crypt(json.dumps(data))
    r = requests.post(url, data={"request": data, "bc": bc})
    return r.json()


def send_code(host, mobile):
    data = {
        "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 1014, "cmdName": "h5_zz",
                   "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": "",
                   "platformCode": "h5mobile", "token": ""}, "body": {"mobile": mobile, "tokenId": ""}}
    url = "https://user-api." + host + ".com/user/public/securityMobileHandler.do"
    if host == "qiuku8":
        r = en_post(url, data)
    else:
        r = en_post(url, data, bc="cy")
    time.sleep(1)
    return r


def get_sms_code(host, mobile):
    # 打开数据库连接
    db = pymysql.connect("172.16.201.4", "root", "jdd.com", "jdd_cpods_sms")
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 使用 execute()  方法执行 SQL 查询
    sql = "select s_body from cpods_sms_message where s_brand_code = %s and s_mobile_number = %s order by d_create_time desc limit 1"
    if host == "qiuku8":
        bc = "qk"
    else:
        bc = "cy"
    cursor.execute(sql, [bc, mobile])
    # db.commit()
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchone()
    print(data)
    # 关闭数据库连接
    db.close()
    code = re.match(r'.*?(\d+)', data[0]).group(1)
    print(code)
    return code

#【-】您的验证码是:243513,请尽快完成验证。

def login(host, mobile, code):
    url = "https://user-api." + host + ".com/user/public/securityMobileHandler.do"
    if host == "qiuku8":
        data = {"header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 1016,
                           "cmdName": "h5_zz",
                           "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": "",
                           "platformCode": "h5mobile", "token": ""}, "body": {"mobile": mobile, "verifycode": code}}
        r = en_post(url, data)
        if r.get('code') == -12:
            data = {"header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 10130,
                               "cmdName": "h5_zz",
                               "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": "",
                               "platformCode": "h5mobile", "token": ""}, "body": {"mobile": mobile}}
            r = en_post(url, data)
    else:
        data = {"header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 1016,
                           "cmdName": "cy_h5_zz",
                           "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": "",
                           "platformCode": "h5mobile", "token": ""}, "body": {"mobile": mobile, "verifycode": code}}
        r = en_post(url, data, bc="cy")
        if r.get('code') == -12:
            data = {"header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 10130,
                               "cmdName": "cy_h5_zz",
                               "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": "",
                               "platformCode": "h5mobile", "token": ""}, "body": {"mobile": mobile}}
            r = en_post(url, data, bc="cy")
    token = r["data"].get("token")
    id = r["data"].get("id")
    return token, id


def user_data(host, num):
    for _ in range(num):
        while True:
            mobile = create_phone()
            r = send_code(host, mobile)
            if r['code'] != 0:
                pass
            else:
                break
        code = get_sms_code(host, mobile)
        token, id = login(host, mobile, code)
        userid = base64.b64decode(id).decode()
        data = {'userid': userid, 'token': token, 'id': id}
        print(mobile, id, userid)
        yield data


#   登录交易系统,返回cookie
def Login_Trade():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('-lang=zh-cn')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get(r"http://cas.jdd.com/login?service=http%3A%2F%2Fbms.qiuku8.com%2Ftrade%2F")
    browser.find_element_by_id("username").send_keys("admin")
    browser.find_element_by_id("password").send_keys("111111")
    browser.find_element_by_id("login").click()
    cookie = browser.get_cookies()[0]["value"]
    print(browser.get_cookies())
    browser.quit()
    return cookie


def order_detail(host, scheme_id):
    data = {
        "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 5001, "cmdName": "h5_zz",
                   "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": "",
                   "platformCode": "h5mobile", "token": ""}, "body": {"schemeId": scheme_id}}
    url = "https://order-api." + host + ".com/order/public/securityMobileHandler.do"
    if host == "qiuku8":
        r = en_post(url, data)
    else:
        r = en_post(url, data, bc="cy")
    leftcount = r['data']['leftCount']
    unitmoney = r['data']['unitMoney']
    return leftcount, unitmoney


def hemai(host, userid, token, scheme_id, leftcount, unitmoney):
    if leftcount > 1:
        buy_count = random.randint(1, leftcount // 2 if leftcount // 2 < 10 else 10)
    else:
        buy_count = 1
    buy_money = round(unitmoney * buy_count, 2)
    data = {
        "header": {"appVersion": "4.0.2", "cmdId": 0, "platformVersion": "4.0.2", "action": 5051, "cmdName": "h5_zz",
                   "agencyId": "", "userType": 1, "uuid": "695d4f722d574544ae836f064f2774d5", "userID": userid,
                   "platformCode": "h5mobile", "token": token},
        "body": {"schemeId": scheme_id, "buyMoney": buy_money, "buyCount": buy_count}}
    url = "https://order-api." + host + ".com/order/public/securityMobileHandler.do"
    if host == "qiuku8":
        r = en_post(url, data)
    else:
        r = en_post(url, data, bc="cy")
    print(r)


def recharge_hemai(host, scheme_id, number):
    cookie = Login_Trade()
    header = {"Cookie": "SESSION=" + cookie, "Content-Type": "application/json"}
    for user in user_data(host, number):
        data = {"userId": user['userid'], "money": str(1000), "buyType": 1, "remark": "test"}
        r = requests.post(
            "http://bms.qiuku8.com/trade/trade/private/tradeSystemPayController/systemPayForUser.do",
            headers=header,
            data=json.dumps(data))
        leftcount, unitmoney = order_detail(host, scheme_id)
        if leftcount > 0:
            hemai(host, user['id'], user['token'], scheme_id, leftcount, unitmoney)
        else:
            break


if __name__ == '__main__':
    host = 'qiuku8'
    scheme_id = '57712166'
    recharge_hemai(host, scheme_id, 1)
