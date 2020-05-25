# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/5/21 19:47
@File:origin_dir.py
"""
import os
current_path = os.path.abspath((os.path.dirname(os.path.dirname(__file__))))
report_path = os.path.abspath(os.path.join(current_path,"report"))
log_path = os.path.abspath(os.path.join(current_path,"logs"))
#print(report_path,current_path)
if not os.path.exists(report_path):
   os.mkdir(report_path)
if not os.path.exists(log_path):
    os.mkdir(log_path)
data_path = os.path.abspath(os.path.join(current_path,"params"))
if not os.path.exists(data_path):
    os.mkdir(data_path)
