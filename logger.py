# -*- coding=utf-8 -*-
"""
@Destrible:
@Author:hamioo
@Time:2020/6/24 13:44
@File:logger.py
"""
import sys


class Logger(object):
    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


sys.stdout = Logger(logs/a.log, sys.stdout)
sys.stderr = Logger(logs/a.log, sys.stderr)  # redirect std err, if necessary

# now it works
print("print something")
