# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/5/25 14:57
@File:config.py
"""
import configparser
import os
parentDirPath=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#parent_dir = os.path.dirname(os.path.dirname(__file__))
#current_file = os.path.abspath(os.path.join(parent_dir, 'config/conf_local.ini'))
current_file = parentDirPath+'\\config\\config_local.ini'
print(current_file)
conf = configparser.ConfigParser()
conf.read(current_file, encoding="utf-8")


class Mysql:
    host = conf.get('DB', 'host')
    port = conf.get('DB', 'port')
    user = conf.get('DB', 'user')
    password = conf.get('DB', 'password')
    db_name = conf.get('DB', 'db_name')


# if __name__ == "__main__":
#     print(Mysql.host)
