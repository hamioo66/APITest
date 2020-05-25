# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/5/25 14:57
@File:config.py
"""
import configparser
import os

parent_dir = os.path.dirname(os.path.dirname(__file__))
current_file = os.path.abspath(os.path.join(parent_dir, 'config/conf_local.ini'))
conf = configparser.ConfigParser()
conf.read(current_file, encoding="utf-8")


class Mysql():
    host = conf.get("DBconf", "host")
    port = conf.get("DBconf", "port")
    user = conf.get("DBconf", "user")
    password = conf.get("DBconf", "password")
    db_name = conf.get("DBconf", "db_name")
