import json

import requests
import time
import random
from common.util_py3 import Prpcrypt

# header = {
#     'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
#     'Referer': 'https://h5.duoduoyoucai.com/lottery/pages/news/news',
#     'Host': 'api.duoduoyoucai.com',
#     'Origin': 'https://h5.duoduoyoucai.com',
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
# }
# url = 'https://api.duoduoyoucai.com/carina/unct/public/handler'
url = 'https://data2c.jdddata.com/number/info/list/v1'

parms = {"header":{"appVersion":"4.0.2","cmdId":0,"platformVersion":"4.0.2","action":1009,"cmdName":"h5_zz","uuid":"223b261716f84bc19d3b005ed22b834e","brand":"szcapp","platformCode":"h5mobile"},"body":{"timeStamp":"","size":10,"labels":"2|3|4|5|6|7|8"}}


def get_response(url, data=None, json=None):
    try:

        response = requests.post(url, data=data, json=json)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response
    except Exception as e:
        print('请求异常，错误信息:%s' % e)
        return None

# 加密
def AES_parameter(kwargs):
    pc = Prpcrypt('d3YmI1BUOSE2S2YmalBVZUQ=', '0000000000000000')
    dict_to_json = json.dumps(kwargs, sort_keys=True)
    e = pc.encrypt(dict_to_json)
    return e

def common(size, page=None, timeStamp=None, batchNumber=None, title=None):
    print('page:%s, timeStamp:%s, batchNumber:%s' % (page, timeStamp, batchNumber))
    if timeStamp:
        parms['body']['timeStamp'] = timeStamp
    if batchNumber or batchNumber != '0':
        parms['body']['batchNumber'] = batchNumber
    if page:
        parms['body']['page'] = str(page)
    else:
        page = 1
    parms['body']['size'] = size
    aes_parms = AES_parameter(parms)
    response = get_response(url, data={'request': aes_parms})
    if not response:
        print('接口返回异常，请求参数:%s' % aes_parms)
        return
    res = response.json()
    request_time = response.elapsed.total_seconds()
    with open('file/requestTime.txt', 'a', encoding='utf-8')as f1:
        f1.write('title：%s，page：%s，size：%s, 响应时间：%s，时间戳：%s，batchNumber：%s，请求参数：%s \n' % (title, page, size, request_time, timeStamp, batchNumber, parms))
    return res


def monitor_news(pageCount):
    if 1 == pageCount:
        for size in [10, 15]:
            if 10 == size:
                res = common(size)
                news = res['data'][-1]
                timeStamp = news.get('timeStamp')
                batchNumber = news.get('batchNumber')
                title = news.get('title').replace(',', '')
                with open('file/timeStamp10.txt', 'w', encoding='utf-8')as f10:
                    f10.write(timeStamp+','+batchNumber+','+title)
            else:
                res = common(size)
                news = res['data'][-1]
                timeStamp = news.get('timeStamp')
                batchNumber = news.get('batchNumber')
                title = news.get('title').replace(',', '')
                with open('file/timeStamp15.txt', 'w', encoding='utf-8')as f15:
                    f15.write(timeStamp+','+batchNumber+','+title)

    else:
        for size in [10, 15]:
            if 10 == size:
                with open('file/timeStamp10.txt', 'r', encoding='utf-8')as f10:
                    content = f10.read()
                if content:
                    timeStamp, batchNumber, title = content.split(',')
                    res = common(size, pageCount, timeStamp, batchNumber, title)
                    news = res['data'][-1]
                    new_timeStamp = news.get('timeStamp')
                    new_batchNumber = news.get('batchNumber')
                    new_title = news.get('title').replace(',', '')
                    with open('file/timeStamp10.txt', 'w', encoding='utf-8')as f10:
                        f10.write(new_timeStamp+','+new_batchNumber+','+new_title)
                else:
                    with open('file/requestTime.txt', 'a', encoding='utf-8')as f:
                        f.write('page：%s，size：%s，接口响应时间获取失败，时间戳和batchNumber为空 \n' % (pageCount, size))
                        print('page：%s，size：%s，接口响应时间获取失败，时间戳和batchNumber为空 \n' % (pageCount, size))
                        return
            else:
                with open('file/timeStamp15.txt', 'r', encoding='utf-8')as f15:
                    content = f15.read()
                if content:
                    timeStamp, batchNumber, title = content.split(',')
                    res = common(size, pageCount, timeStamp, batchNumber, title)
                    news = res['data'][-1]
                    new_timeStamp = news.get('timeStamp')
                    new_batchNumber = news.get('batchNumber')
                    new_title = news.get('title').replace(',', '')
                    with open('file/timeStamp15.txt', 'w', encoding='utf-8')as f15:
                        f15.write(new_timeStamp+','+new_batchNumber+','+new_title)
                else:
                    with open('file/requestTime.txt', 'a', encoding='utf-8')as f:
                        f.write('page：%s，size：%s，接口响应时间获取失败，时间戳和batchNumber为空 \n' % (pageCount, size))
                        print('page：%s，size：%s，接口响应时间获取失败，时间戳和batchNumber为空 \n' % (pageCount, size))
                        return


if __name__ == '__main__':
    count = 1
    while True:
        for i in range(1, 17):
            print('正在请求第%s页' % i)
            monitor_news(i)
            time.sleep(random.randint(1, 5))
        with open('file/requestTime.txt', 'a', encoding='utf-8')as f:
            f.write('\n')
        print('跑完第%s轮' % count)
        count += 1
        time.sleep(random.randint(310, 360))
