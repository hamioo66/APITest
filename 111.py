# msg = input('请输入一个字符串\n')
# str1 = msg.split(' ')[1]
# print(len(str1))
# str2 = msg.split(' ').pop()
# print(len(str2))
# print(str2)

# 计算字符串最后一个单词的长度，单词以空格隔开。
# str = input().strip().split()
# print(type(str))
# print(len(str[len(str)-1]))
#
#
# s = 'hello wOrld'
# print(s.count('o')+s.count('O'))

"""写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。"""
# 方法1
# str = input().lower()
# str2 = input().lower()
# print(str.count(str2))

# 方法2
# str = input().upper()
# str3 = input().upper()
# str2 = list(str)
# count = 0
# for i in range(len(str2)):
#     if str2[i] == str3:
#         count += 1
# print(count)


# import random
# n = int(input())
# l = []
# for i in range(n):
#     num = random.randint(1,1000)
#     print(num)
#     l.append(num)
#     l = list(set(l))
#     l.sort()
# print(l)
"""

"""
# while True:
#     try:
#         n = int(input())
#         b = []
#         for i in range(n):
#             l = int(input())
#             b.append(l)
#         b1 = list(set(b))
#         b1.sort()
#         for i in range(len(b1)):
#             print(b1[i])
#     except:break
#
# while True:
#     try:
#         a, res = int(input()), set()
#         for i in range(a):
#             res.add(int(input()))
#         for i in sorted(res):
#             print(i)
#     except:
#         break

#
# while True:
#     str = input()
#     while 100 > len(str) >= 8:
#         print(str[:8])
#         str = str[8:]
#     if 0 < len(str) < 8:
#         print(str + '0' * (8 - len(str)))
#     else:
#         if len(str) == 0 and len(str) >= 100:
#             pass

# while True:
#     try:
#         str = input()
#         print(int(str,16))
#     except:
#         break


# def fun(n):
#     list1 = []
#     for i in range(2,n):
#         for j in range (2,i):
#             if i%j == 0:
#                 break
#         else:#这里的else承接的是for循环里的条件判断
#             list1.append(i)
#     return list1.strip().split(' ')
# n=int(input('输入一个数：'))
# print(fun(n))

"""
取一个数的质因子
"""
# def fun(n):
#     list1 = []
#     for i in range(2,n//2+1):
#         while n % i == 0:
#             list1.append(i)
#             list2 = map(str,list1)
#             n = n / i
#     return " ".join(list2)+" " if list1 else str(n) + " "
# n = int(input())
# print(fun(n))
"""
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整
"""

# i = float(input())
# while i > 0.0:
#     try:
#         j=str(i).split('.')[1]
#         n = str(i).split('.')[0]
#         if int(j) >=5:
#             i = int(n)+1
#         else:
#             i = input(n)
#         print(i)
#     except:
#         break

"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
"""
import sys

# n = int(input())
# s = {}
# for i in range(n):
#     lines = sys.stdin.readline().strip().split(' ')
#     print(lines)
#     k = int(lines[0])
#     v = int(lines[1])
#     if k in s:
#         s[k] = s[k] + v
#     else:
#         s[k] = v
# ss = s.keys()
# for k in ss:
#     print(k, s[k])

# def square(x) :            # 计算平方数
#     return x ** 2
# for i in map(square, [1,2,3,4,5]):
#     b=map(square, [1, 2, 3, 4, 5])
#     print(i,type(b))
# print()

"""
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
import sys
#a = sys.stdin.readline()
"""

# i, str1 = int(input()), ""
# for _ in str(i)[::-1]:
#     if _ not in str1:
#         str1 = str1 + _
# new = "".join(str1)
# print(int(new))


# str, j = input(), 0
# for i in list(str):
#     if 0 < ord(i) < 127 and ord(i)!=10:
#         j = j + 1
#         print(i)
#         #pass
# #print(ord('\n'))
# print(j)
#
# print(input()[::-1])
#
# print(input())
# a = int(input())
# b = bin(a)
# #print(b)
# c = 0
# for i in b:
#     if i == '1':
#         c+=1
# print(c)
#
# from log.log import log
# log.info('556525555')
# print(round(1.1135, 3))
# print(round(1.1125, 3))
# print(round(1.675, 2))
"""
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
# 格式化输出
# age = 18
# print('我的名字是%s，我的国籍是%s'%("小张","中国"))
# print("我的年级是：%d岁"%age)
# print("aaa","bbb","ccc")
# print("www","baidu","com",sep=".")
# print("hello",end="")
# print("world",end="\t")
# print("python",end="\n")
# print("end")

# password = input("请输入密码:")
# print("您刚刚输入的密码是:",password)
# print(type(password))
# if True:
#     print("True")
# else:
#     print("False")
# i = 1
# sum = 0
# while i < 101:
#     sum = sum+i
#     i = i+1
# print(sum)


# #增
# info = {"name":"吴彦祖","age":8}
# newID = input("请输入新的学号")
# info["id"] = newID
# print(info["id"])
# #删
# info = {"name":"吴彦祖","age":8}
# print("删除前：%s"%info["name"])
# del info["name"]
# print("删除后：%s"%info)
# 改
# 查
from bs4 import BeautifulSoup  # 网页解析获取数据
import re  # 正则白哦大师，进行文字匹配
import urllib.request, urllib.error  # 指定url获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行sqllite数据库操作
import urllib.parse


# 获取一个post请求
# try:
#     data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="UTF-8")
#     response = urllib.request.urlopen("http://httpbin.org/post", data=data,timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out")
#
#获取一个get请求
try:
    response = urllib.request.urlopen("http://www.baidu.com",timeout=0.01)
    print(response.read().decode('utf-8'))
except urllib.error.URLError as e:
    print("time out")



# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.headers)
# print(response.getheader("Server"))
#
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
# url = "https://www.douban.com"
# #data=bytes(urllib.parse.urlencode({"name":"hamioo"}), encoding="UTF-8")
# req = urllib.request.Request(url=url,headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

file = open("./baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")
# print(bs.title)
# print(bs.title.string)
# print(bs.a.attrs)
#
# # 文档的遍历
# print(bs.head.contents)
#
# print(bs.head.contents[1])

#文档的搜索
#find_all()
#字符串过滤：会查找与字符串完全匹配的内容
#t_list = bs.find_all("a")

#正则表达式搜索：使用search()方法匹配内容
# t_list = bs.find_all(re.compile("a"))

#传入一个函数，根据函数的要求搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list = bs.find_all(name_is_exists)

#kwargs 参数
# t_list = bs.find_all(id = "head")
t_list = bs.find_all(text=re.compile("\d"))
for item in t_list:
    print(item)
