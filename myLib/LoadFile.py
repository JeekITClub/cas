# -*- coding:GBK -*-
import xlrd
import Student

# 常量声明
ClassNum = 13


# 读入学生信息，返回stuList列表
def LoadFile(fileName):

    data = xlrd.open_workbook(fileName)
    stuList = [Student for i in range(0, 1400)]

    for i in range(0, ClassNum):
        table = data.sheets()[i]
        for j in range(1, table.nrows):
            subject = []
            num = table.cell(j, 0)
            name = table.cell(j, 1)
            for k in range(2, 11):
                subject.append(table.cell(j, k))
            stuList[int(num % 10000)] = Student.Student(num, name, subject)

    return stuList
