# -*- coding=utf-8 -*-
"""
@Destrible:数据库连接
@Author:hamioo
@Time:2020/5/25 16:55
@File:db.py
"""
from builtins import Exception

import pymysql
from common.config import Mysql


class DB:
    def __init__(self):
        mysql = Mysql()
        try:
            self.conn = pymysql.connect(host=mysql.host, port=int(mysql.port), user=mysql.user, password=mysql.password,
                                        database=mysql.db_name,charset='utf8')
            self.cursor = self.conn.cursor()
        except Exception as e:
            print("数据库连接失败：%s"% e)
    def executesql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def closesql(self):
        self.cursor.close()
        self.conn.close()
#
# if __name__ =="__main__":
#     d = DB()
