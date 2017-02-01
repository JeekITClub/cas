# -*- coding:utf-8 -*-
import xlrd
import os

import student

# 常量声明
ClassNum = 13


# 班级数量暂定为常量

#检查文件错误，正常返回False，有误返回True
def check_error(filename):
    #文件不存在
    if not os.path.exists(filename):
        print('文件不存在！')
        return True
    # 检查表格是否错误的函数
    else:
        data = xlrd.open_workbook(filename)
        pass
    #检查是否符合要求，填写是否有问题


# 读入学生信息，返回stuList列表
def load_file(filename):
    if check_error(filename):
        return 1
    data = xlrd.open_workbook(filename)
    stulist = [student for i in range(0, 1400)]

    for i in range(0, ClassNum):
        table = data.sheets()[i]
        for j in range(1, table.nrows):
            subject = []
            num = table.cell(j, 0)
            name = table.cell(j, 1)
            for k in range(2, 11):
                subject.append(table.cell(j, k))
            stulist[int(num % 10000)] = student.Student(num, name, subject)

    return stulist
