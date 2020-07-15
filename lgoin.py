# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/11/20
describle:用户登录接口
"""
import requests
import json
from utils import util_py3


class web_requests(object):
    def __init__(self):
        pass

    def Interface(self):
        # https: // user - api.baoying518.com / user / public / securityMobileHandler.do
        url = "https://user-api.baoying518.com/user/public/securityMobileHandler.do"
        headers = {"appVersion": "6.0.1",
                   "idfa": "",
                   "cmdName": "app_zz",
                   "userID": "",
                   "uuid": "ffffffff-99bd-8d7f-8930-7ad40033c587",
                   "token": "",
                   "cmdID": "0",
                   "platformVersion": "6.0",
                   "imei": "868406028925956",
                   "action": "1011",
                   "userType": "1",
                   "platformCode": "Android",
                   "phoneName": "HUAWEI",
                   }
        data = {"name": "", "pw": "", "usertype": "1"}
        name = "15599155289"
        password = "aaaaaa"
        data["name"] = name
        data["pw"] = password
        print(data)
        request = "2Rc75HULvIxtcnOZfmdp8RZMOJTeTqBhKd3iDur1ajQzxVlcfcWvgUc9Uh8MT5rQa6DI1xYu3itBv48JXKrwYzQI5PXCD/1v8h7r1ufyBkLvvdYzLwmd/MncuCaV8h755c+LG0fx5FKuINhAld0TyXjj48/YXAZZxVH7TwWsXyU4gLSET6jsDUe2WT37+i9PzGlbhqMY0vIHMzkeNNiAZVEerj1xLM+45wutrQMTCGbLMFsjadVDHQB4DUnabrgZTWjHRYfKFTeKwwfQIdrUs6+wag92MenTmlU4n1c3wDdt1LwUyYvu6jBBPhXY5Z/gByPfh6bGL5mlHw77pt6uVUbwBD01eA/H06Bx6jbJzPnPyAcroFEI7wtk0cVg1qYm7Cdzbx3tR7MnEqCuJ8BmnrJSxqVNHbzVwEead+aNGAfuQk4zDmDwqwQ+1ss0GZm5+fICmd/Ws1ry0CACtilRZg=="
        pc = util_py3.Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', '0000000000000000')
        e = pc.decrypt(request)
        print(e)
        r = requests.post(url=url, data=request)
        print(r.text)
        print(r.status_code)
        l = json.dumps(json.loads(r.text), ensure_ascii=False)
        print(l)


a = web_requests()
a.Interface()
