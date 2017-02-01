# Package for settings
# coding=utf-8
import json


class Settings:
    item=""
    def __init__(self):
        self.item=""

    def check_error(self, data):
        pass

    def read_json(self,item):
        # subject要读取的项目，teachers,settings,classroom 还是students
        if item=="teachers":
            data=json.JSONEncoder()
            #这里还需要看下json模块的文档
        elif item=="classroom":
            data=json.JSONEncoder()
        elif item=="settings":
            data=json.encoder.JSONEncoder([ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ])
            print data

#???????????JSON这里的语法还没弄清楚

