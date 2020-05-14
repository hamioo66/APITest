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
#         str = input()
#         while len(str) >= 8:
#             print(str[:8])
#             str = str[8:]
#         if 0 < len(str) < 8:
#             print(str + '0' * (8 - len(str)))
#         else:
#             if len(str) == 0:
#                 pass

# while True:
#     try:
#         str = input()
#         print(int(str,16))
#     except:
#         break


