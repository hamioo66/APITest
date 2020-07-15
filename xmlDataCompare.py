# -*- coding=utf-8 -*-
"""
@Destrible:
http://lottery-inner.jiangduoduo.com/byte_dance/highfreq/result/one
http://114.118.2.15/byte_dance/highfreq/result/one?pCode=analysisJob
@Author:hamioo
@Time:2020/6/24 10:38
@File:xmlDataCompare.py
"""
from utils.util_py3 import Prpcrypt
import requests
import json
import difflib

# import sys
# f = open('logs/a.log', 'a')
# sys.stdout = f
"""
比对测试和线上数据
"""


def get_dif_one(url, urlTest, key, file):
    with open(file, 'r', encoding='utf-8') as w:
        lines = w.readlines()
        for line in lines:
            lotteryName = line.split(':')[0]
            lotteryId = line.split(':')[1]
            data = {"name": lotteryName}
            # print(lotteryName)
            Jdata = json.dumps(data, sort_keys=True)
            request = Prpcrypt(key, "0000000000000000").encrypt(Jdata)
            response = requests.post(url, data={'request': request})
            responseTest = requests.post(urlTest, data={'request': request})
            a = response.text
            b = responseTest.text
            d = difflib.Differ()
            print(f'**********************当前彩种{lotteryName}**********************' + '\n')
            # diff = difflib.ndiff(a.splitlines(keepends=True),b.splitlines(keepends=True))
            diff = d.compare(a.splitlines(keepends=True), b.splitlines(keepends=True))
            # print(a, b)
            print(''.join(diff), end="")
            # print(''.join(
            #     difflib.context_diff(a.splitlines(keepends=True), b.splitlines(keepends=True), '线上', '测试')),
            #       end="")


"""
搜狗query
"""


def get_dif_query(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            lotteryName = line.split(':')[0]
            lotteryId = line.split(':')[1].split('\n')[0]
            query_url = 'https://lottery-inner.jiangduoduo.com/sogou/query/lottery?id={}&app_id=cp001&timestamp=1592884266977&sign=76da4967277431219f2cccb7089b766a'
            query_url = query_url.format(lotteryId)
            urlTest = query_url.replace('https://lottery-inner.jiangduoduo.com', 'http://114.118.2.15')
            response = requests.get(query_url)
            responseTest = requests.get(urlTest)
            a = response.text
            b = responseTest.text
            d = difflib.Differ()
            print(f'**********************当前彩种{lotteryName}**********************' + '\n')
            # diff = difflib.ndiff(a.splitlines(keepends=True),b.splitlines(keepends=True))
            diff = d.compare(a.splitlines(keepends=True), b.splitlines(keepends=True))
            # print(a, b)
            print(''.join(diff), end="\n")
            # print(''.join(
            #     difflib.context_diff(a.splitlines(keepends=True), b.splitlines(keepends=True), '线上', '测试')),
            #       end="")


def get_diff_other(url, urlTest):
    response = requests.get(url)
    responseTest = requests.get(urlTest)
    a = response.text
    b = responseTest.text
    d = difflib.Differ()
    # diff = difflib.ndiff(a.splitlines(keepends=True), b.splitlines(keepends=True))
    # diff = difflib.context_diff(a.splitlines(keepends=True),b.splitlines(keepends=True))
    diff = d.compare(a.splitlines(keepends=True), b.splitlines(keepends=True))
    # diff = difflib.unified_diff(a.splitlines(keepends=True), b.splitlines(keepends=True))
    # print(a, b)
    print(''.join(diff), end="")
    # print(''.join(
    #     difflib.context_diff(a.splitlines(keepends=True), b.splitlines(keepends=True), '线上', '测试')),
    #       end="")


if __name__ == "__main__":
    highLottery = 'file/highLotteryName.txt'  # 高频彩
    nationLottey = 'file/nationLotteryName.txt'  # 全国彩
    key = 'd8YmI1BUZSE3S3YmalBVZUQ='
    key1 = 'd3YmI1BUOSE2S2YmalBVZUQ='
    url = 'https://lottery-inner.jiangduoduo.com/byte_dance/highfreq/result/one'
    urlTest = 'http://114.118.2.15/byte_dance/highfreq/result/one?pCode=analysisJob'
    url1 = 'https://lottery-inner.jiangduoduo.com/sogou/query/lottery?app_id=cp001&timestamp=1592884266977&sign=76da4967277431219f2cccb7089b766a&id='
    urlTest1 = 'http://114.118.2.15/sogou/query/lottery?app_id=cp001&timestamp=1592884266977&sign=76da4967277431219f2cccb7089b766a&id='
    """
    uc:
    高频：http://114.118.2.15/uc/highfreq  1
    非高频：http://114.118.2.15/uc/nonhighfreq 1
    竞彩：http://114.118.2.15/uc/jingcai  1
             http://114.118.2.15/uc/common  1
    uc:
    高频：http://lottery.jiangduoduo.com/uc/highfreq
    非高频：http://lottery.jiangduoduo.com/uc/nonhighfreq
    竞彩：http://lottery.jiangduoduo.com/uc/jingcai
             http://lottery.jiangduoduo.com/uc/common      
    搜狗
    非高频 http://114.118.2.15/sogou/lottery/nonhighfreq  1
    高频 http://114.118.2.15/sogou/lottery/highfreq  1
    综合 http://114.118.2.15/sogou/lottery/complex   1
    竞彩 http://114.118.2.15/sogou/lottery/jingcai   1
    走势 http://114.118.2.15/sogou/lottery/trend   1
        http://114.118.2.15/sogou/lottery/play    1
        http://114.118.2.15/sogou/query/lottery?id=1001&app_id=cp001&timestamp=1592884266977&sign=76da4967277431219f2cccb7089b766a   1

    搜狗
    非高频 http://lottery.jiangduoduo.com/sogou/lottery/nonhighfreq
    高频 http://lottery.jiangduoduo.com/sogou/lottery/highfreq
    综合 http://lottery.jiangduoduo.com/sogou/lottery/complex
    竞彩 http://lottery.jiangduoduo.com/sogou/lottery/jingcai
    走势 http://lottery.jiangduoduo.com/sogou/lottery/trend
        http://lottery.jiangduoduo.com/sogou/lottery/play
        https://lottery-inner.jiangduoduo.com/sogou/query/lottery?id=1001&app_id=cp001&timestamp=1592884266977&sign=76da4967277431219f2cccb7089b766a
    
    头条
    http://114.118.2.15/byte_dance/lottery  1
    http://114.118.2.15/byte_dance/highfreq?pCode=analysisJob   1
    http://114.118.2.15/byte_dance/highfreq/result?pCode=analysisJob  1
    http://114.118.2.15/byte_dance/highfreq/result/v2?pCode=analysisJob  1
    http://114.118.2.15/byte_dance/highfreq/result/list?pCode=analysisJob  1
    http://114.118.2.15/byte_dance/lottery/result    1
    http://114.118.2.15/byte_dance/highfreq/result/one  post   request:"FfkC2SRDUHq0WgtEfhp+AWAv/xc+vg9jqwqkrjnAv0k="  1
    
    头条
    http://lottery.jiangduoduo.com/byte_dance/lottery
    http://lottery.jiangduoduo.com/byte_dance/highfreq?pCode=analysisJob
    http://lottery.jiangduoduo.com/byte_dance/highfreq/result?pCode=analysisJob
    http://lottery.jiangduoduo.com/byte_dance/highfreq/result/v2?pCode=analysisJob
    http://lottery.jiangduoduo.com/byte_dance/highfreq/result/list?pCode=analysisJob
    http://lottery.jiangduoduo.com/byte_dance/lottery/result   
    http://lottery.jiangduoduo.com/byte_dance/highfreq/result/one  post   request:"FfkC2SRDUHq0WgtEfhp+AWAv/xc+vg9jqwqkrjnAv0k="
    
    百度：
    http://114.118.2.15/baidu/country   1   lastmod时间不一致
    http://114.118.2.15/baidu/country/1   作废
    http://114.118.2.15/baidu/local
    http://114.118.2.15/baidu/local/nonhighfreq  1
    http://114.118.2.15/baidu/local/nonhighfreq/1    1
    http://114.118.2.15/baidu/zucai  
    http://114.118.2.15/baidu/zucai/sitemap   1
    http://114.118.2.15/baidu/trend/v2      #post参数不明
    
    百度：
    http://lottery.jiangduoduo.com/baidu/country
    http://lottery.jiangduoduo.com/baidu/country/1   返回空  
    http://lottery.jiangduoduo.com/baidu/local   1
    http://lottery.jiangduoduo.com/baidu/local/nonhighfreq
    http://lottery.jiangduoduo.com/baidu/local/nonhighfreq/1
    http://lottery.jiangduoduo.com/baidu/zucai   
    http://lottery.jiangduoduo.com/baidu/zucai/sitemap   
    http://lottery.jiangduoduo.com/baidu/trend/v2  
    """
    url2 = 'http://114.118.2.15/baidu/local?pCode=job'
    urlTest2 = 'http://lottery.jiangduoduo.com/baidu/local?pCode=analysisJob'
    # get_dif_one(url, urlTest, key, highLottery) #头条result/one
    # get_dif_query(nationLottey)   #搜狗query
    get_diff_other(url2, urlTest2)  # uc
