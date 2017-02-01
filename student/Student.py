# -*- coding:utf-8 -*-


class Student:
    num = 0  # 学号
    name = ''  # 姓名
    subject = []  # 选科
    pclass = 0  # 学生所在行政班
    tclass = 0  # 学生所在教学班

    def __init__(self, num, name, subject, pclass, tclass):
        self.num = num
        self.name = name
        self.subject = subject
        self.pclass = pclass
        self.tclass = tclass
