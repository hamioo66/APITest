# -*-coding:utf-8 -*-
"""
@Destrible:首页资讯接口
@Author:hamioo
@Time:2020/5/21 16:57
@File:api_002.py
"""

import xlrd
import xlwt
import os
import json
from xlutils.copy import copy
from collections import OrderedDict
from common import origin_dir


class Excel(object):
    def __init__(self, filename=None):
        if not os.path.exists(filename):
            self.filename = os.path.join(origin_dir.data_path, filename).replace("\\", "/")
        else:
            self.filename = filename
        self.test_data = xlrd.open_workbook(self.filename, formatting_info=True)
        self.sheet = self.test_data.sheet_by_index(0)

    def get_row(self):
        row = self.sheet.nrows
        return row

    def get_col(self):
        return self.sheet.ncols

    def get_url(self, row):
        return self.sheet.cell_value(row, 0)

    def get_data(self, row):
        cell_value = self.sheet.cell_value(row, 2)
        try:
            data = json.loads(cell_value, object_pairs_hook=OrderedDict, strict=False)
        except json.decoder.JSONDecodeError:
            raise Exception("json解析失败，请检查入参格式")
        else:
            return data

    def get_header(self, row):
        return eval(self.sheet.cell_value(row, 3))

    def get_excepted_results(self, row):
        excepted_results = self.sheet.cell_value(row, 4)
        return str(excepted_results)

    def get_sign(self, row):
        return self.sheet.cell_value(row, 9)

    def get_datalist(self, col):
        datalist = []
        for i in range(1, self.get_row()):
            datalist.append(self.sheet.cell_value(i, col))
        return datalist

    def insert_data(self, row, col, value):
        borders = xlwt.Borders()
        borders.left = 1
        borders.right = 1
        borders.top = 1
        borders.bottom = 1
        borders.bottom_colour = 0x3A
        style = xlwt.XFStyle()
        style.borders = borders
        olddata = xlrd.open_workbook(self.filename, formatting_info=True)
        newdata = copy(olddata)
        newtable = newdata.get_sheet(0)
        newtable.write(row, col, str(value), style)
        newdata.save(self.filename)

    def insert_excepted_results(self, row, value):
        self.insert_data(row, 4, value)

    def insert_responsetime(self, row, value):
        self.insert_data(row, 5, value)

    def insert_statuscode(self, row, value):
        self.insert_data(row, 6, value)

    def insert_results(self, row, value):
        self.insert_data(row, 7, value)

    def insert_comments(self, row, value):
        self.insert_data(row, 8, value)

    def init_data(self):
        for rows in range(1, self.get_row()):
            self.insert_comments(rows, "")
            self.insert_results(rows, "")
            self.insert_responsetime(rows, "")
            self.insert_statuscode(rows, "")
