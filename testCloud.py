# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/7/15 11:02
@File:testCloud.py
"""
import jieba  # 分词
from matplotlib import pyplot  # 绘图，数据可视化
from wordcloud import wordcloud  # 词云
from PIL import Image  # 图片处理
import numpy  # 矩阵运算
import sqlite3  # 数据库

con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text = text + item[0]
print(text)
