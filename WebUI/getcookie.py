
# -*- coding=utf-8 -*-
"""
@Destrible:利用selenium+phantomjs无界面浏览器的形式访问网站，再获取cookie
@Author:hamioo
@Time:2020/6/9 14:17
@File:getcookie.py
"""
# from selenium import webdriver
# driver = webdriver.PhantomJS()
# cookie_dict = []
# url = 'https://et.xiamenair.com/xiamenair/book/findFlights.action?lang=zh&tripType=0&queryFlightInfo=XMN,PEK,2018-01-15'
# driver.get(url)
# cookie_list = driver.get_cookies()
# for cookie in cookie_list:
#     cookie_dict[cookie['name']]=cookie['value']
#     print(cookie_list)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('-lang=zh-cn') # 不加识别不到元素
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options = chrome_options)
    driver.get(r'http://cas.jiangduoduo.com/login?service=http%3A%2F%2Fcarina-admin.jddods.com%2F')
    #time.sleep(5)
    driver.find_element_by_id("username").send_keys("admin")
    driver.find_element_by_id("password").send_keys("111111")
    driver.find_element_by_id("login").click()
    cookie = driver.get_cookies()[0]["value"]
    print(driver.get_cookies(),cookie)
    #print(driver.page_source,driver.get_cookie('name'))
    driver.close()
if __name__ == '__main__':
    main()
