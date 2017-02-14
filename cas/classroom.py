# coding=utf-8
# 分班程序在此，还有班级管理也在此



class ClassDivision:
    def __init__(self,state=[]):
        self.json={"home":{
            "pcb":{
                "children":False,
                "num":0
            },
            "pcg":{
                "children": False,
                "num": 0
            },
            "pch":{
                "children": False,
                "num": 0
            },
            "pcp":{
                "children": False,
                "num": 0
            },
            "pbg":{
                "children": False,
                "num": 0
            },
            "pbh":{
                "children": False,
                "num": 0
            },
            "pbp":{
                "children": False,
                "num": 0
            },
            "pgh":{
                "children": False,
                "num": 0
            },
            "pgp":{
                "children": False,
                "num": 0
            },
            "php":{
                "children": False,
                "num": 0
            },
            "cbg":{
                "children": False,
                "num": 0
            },
            "cbh":{
                "children": False,
                "num": 0
            },
            "cbp":{
                "children": False,
                "num": 0
            },
            "cgh":{
                "children": False,
                "num": 0
            },
            "cgp":{
                "children": False,
                "num": 0
            },
            "chp":{
                "children": False,
                "num": 0
            },
            "bgh":{
                "children": False,
                "num": 0
            },
            "bgp":{
                "children": False,
                "num": 0
            },
            "bhp":{
                "children": False,
                "num": 0
            },
            "ghp":{
                "children": False,
                "num": 0
            }
        }}
        self.state=state
        self.json["home"]["pcb"]["num"]=state[0]
        self.json["home"]["pcg"]["num"]=state[1]
        self.json["home"]["pch"]["num"]=state[2]
        self.json["home"]["pcp"]["num"]=state[3]
        self.json["home"]["pbg"]["num"]=state[4]
        self.json["home"]["pbh"]["num"]=state[5]
        self.json["home"]["pbp"]["num"]=state[6]
        self.json["home"]["pgh"]["num"]=state[7]
        self.json["home"]["pgp"]["num"]=state[8]
        self.json["home"]["php"]["num"]=state[9]
        self.json["home"]["cbg"]["num"]=state[10]
        self.json["home"]["cbh"]["num"]=state[11]
        self.json["home"]["cbp"]["num"]=state[12]
        self.json["home"]["cgh"]["num"]=state[13]
        self.json["home"]["cgp"]["num"]=state[14]
        self.json["home"]["chp"]["num"]=state[15]
        self.json["home"]["bgh"]["num"]=state[16]
        self.json["home"]["bgp"]["num"]=state[17]
        self.json["home"]["bhp"]["num"]=state[18]
        self.json["home"]["ghp"]["num"]=state[19]


    def Layer2_expand(self,location,expand_nodes_num,solution):
        #这个函数最后要改成所有层所有节点都通用，有待思考

        if self.json["home"][location]["children"]==True:
            pass

        else:
            self.json["home"][location]["children"]={
                "children1":{
                    "children":False,
                    "num":solution[0]
                },
                "children2":{
                    "children":False,
                    "num":solution[1]
                }
            }


    def inherit(self,location):
        #这个函数是当无法进行expand的时候那么继承父级的数据，以保证层数整齐

        pass



    def TreeNodeLayer2(self):
        for key in self.json["home"]:
            if self.json["home"][key]["num"]>=40:
                self.Layer2_expand(key,2,[40,int(self.json["home"][key]["num"])-40])
                #！！！！
            else:
                pass

    def TreeNodeLayer3(self):
        pass

    def division(self):
        pass

    def show(self):
        pass


