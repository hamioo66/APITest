# -*- coding=utf-8 -*-
"""
python 实现列表去重
"""
list = [11,12,13,12,15,16,13]
a = set(list)
print(a)
b = [x for x in a]
print(b)
