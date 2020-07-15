# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/7/8 15:01
@File:testUrllib.py

Flask 框架的核心就是Werkzeug和jinja2
"""
from bs4 import BeautifulSoup  # 网页解析获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 指定url获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqllite数据库操作
import urllib.parse


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    dataList = getData(baseurl)
    # print(dataList)
    # 2.解析数据
    # askUrl(baseurl)
    # 3.保存数据
    # savepath = ".\\豆瓣电梯Top250.xls"
    dbpath = "movie.db"
    # saveData(dataList, savepath)
    saveData2DB(dataList, dbpath)


# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示 规则（字符串的模式）
# 影片图片
findImgSrc = re.compile(r'<img .*src="(.*?)"', re.S)  # re.S让换行符包含在字符中
# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 找到概况
findIng = re.compile(r'<span class="inq">(.*)</span>')
# 找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseurl):
    dataList = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)
        html = askUrl(url)  # 保存获取到的网页源码
        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            # print(item)  # 测试：查看电影item全部信息
            data = []
            item = str(item)  # 保存一部电影的所有信息
            # # 获取影片详情的链接
            link = re.findall(findLink, item)[0]  # re库用来通过正则表达式查找指定的字符串
            data.append(link)

            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)

            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)  # 添加中文名
                otitle = titles[1].replace('/', '')  # 去掉无关的符号
                data.append(otitle)  # 添加外国名
            else:
                data.append(titles[0])
                data.append(' ')  # 外国名留空

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)

            inq = re.findall(findIng, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")

            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)  # 去掉br
            bd = re.sub('/', " ", bd)
            data.append(bd.strip())  # 去掉前后空格

            dataList.append(data)
    # print(dataList)
    return dataList


def askUrl(url):
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉服务器，我们可以接收什么水平的文件）
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    # print(html)
    return html


# 保存数据
def saveData(dataList, savepath):
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建workbook
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 创建工作表
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save(savepath)


def saveData2DB(dataList, dbpath):
    # init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    for data in dataList:
        for index in range(len(data)):
            data[index] = '"' + data[index] + '"'
        sql = '''
        insert into movie250 (
        info_link,pic_link,cname,ename,score,rated,introduction ,info
        )
        values (%s)''' % ",".join(data)
        print(sql)
        cur.execute(sql)
        conn.commit()
    cur.close()
    conn.close()


def init_db(dbpath):
    sql = '''
    create table movie250(
    id integer primary key autoincrement,
    info_link text,
    pic_link text,
    cname varchar,
    ename varcher,
    score numeric,
    rated numeric,
    introduction text,
    info text
    )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # conn.close()
    # cursor.close()


if __name__ == "__main__":
    main()

