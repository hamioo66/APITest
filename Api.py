# -*-coding:utf-8 -*-
import requests
response = requests.get('http://mirrors.sohu.com/')
print(response.text)
