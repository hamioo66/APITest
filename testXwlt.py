# -*- coding=utf-8 -*-
"""
@Destrible:写入excel
@Author:hamioo
@Time:2020/7/9 10:47
@File:testXwlt.py
"""
import xlwt

# workbook  = xlwt.Workbook(encoding="utf-8") #创建workbook
# worksheet = workbook.add_sheet('sheet1') # 创建工作表
# worksheet.write(0,0,'hello')
# workbook.save('student.xls')
workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook
worksheet = workbook.add_sheet('sheet1')  # 创建工作表
for i in range(0, 9):
    for j in range(0, i + 1):
        worksheet.write(i, j, "%d * %d = %d" % (i + 1, j + 1, (i + 1) * (j + 1)))
workbook.save('student.xls')
