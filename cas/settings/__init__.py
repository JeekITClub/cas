# Package for settings
# coding=utf-8

import json


class Settings:
    item=""

    def __init__(self):
        self.item=""

    def read_json(self,item):
        # subject要读取的项目，teachers,settings,classroom 还是students
        file = item+".json"
        fp = open(file, 'r')
        fp_read = json.loads(fp.read())
        #这里要进行检查
        return fp_read
        fp.close()