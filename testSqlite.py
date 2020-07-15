# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/7/9 11:24
@File:testSqlite.py
"""
import sqlite3

conn = sqlite3.connect('test.db')  # 打开或创建数据库文件
print("成功打开数据库")
c = conn.cursor()  # 获取游标
sql = '''
create table company
(id int primary key not null,
name text not null,
age int not null,
address char(50),
salary real );
'''
sql1 = '''
insert into company(id,name,age,address,salary)
values (1,"hamioo",28,"重庆",15000)
'''
sql2 = "select id,name,address,salary from company"
cursor = c.execute(sql2)  # 执行sql语句
for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address =",row[2])
    print("salary = ",row[3])
conn.commit()  # 提交数据库操作
conn.close()  # 关闭数据连接
print("成功建表")
