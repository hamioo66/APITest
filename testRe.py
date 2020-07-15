# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/7/8 15:01
@File:testRe.py
"""
import re
#创建模式对象
pat = re.compile("AA")
m = pat.search("ABCAADDCAAA")
print(m)
print(re.search("asd","Aasd"))
print(re.findall("a","ASdaFaA"))
a = r"\aabd-\ "
print(a)
