# coding=utf-8
# 分班程序在此，还有班级管理也在此



class ClassDivision:
    def __init__(self,state=[],students_num,class_num,class_students_num_region=[40,40]):
        self.json={
            "home":{
            "layer_num":2
            "layer1":｛
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
            },
            "layer2:"{
            }
        }
        self.state=state
        self.json["home"]["layer1"]["pcb"]["num"]=state[0]
        self.json["home"]["layer1"]["pcg"]["num"]=state[1]
        self.json["home"]["layer1"]["pch"]["num"]=state[2]
        self.json["home"]["layer1"]["pcp"]["num"]=state[3]
        self.json["home"]["layer1"]["pbg"]["num"]=state[4]
        self.json["home"]["layer1"]["pbh"]["num"]=state[5]
        self.json["home"]["layer1"]["pbp"]["num"]=state[6]
        self.json["home"]["layer1"]["pgh"]["num"]=state[7]
        self.json["home"]["layer1"]["pgp"]["num"]=state[8]
        self.json["home"]["layer1"]["php"]["num"]=state[9]
        self.json["home"]["layer1"]["cbg"]["num"]=state[10]
        self.json["home"]["layer1"]["cbh"]["num"]=state[11]
        self.json["home"]["layer1"]["cbp"]["num"]=state[12]
        self.json["home"]["layer1"]["cgh"]["num"]=state[13]
        self.json["home"]["layer1"]["cgp"]["num"]=state[14]
        self.json["home"]["layer1"]["chp"]["num"]=state[15]
        self.json["home"]["layer1"]["bgh"]["num"]=state[16]
        self.json["home"]["layer1"]["bgp"]["num"]=state[17]
        self.json["home"]["layer1"]["bhp"]["num"]=state[18]
        self.json["home"]["layer1"]["ghp"]["num"]=state[19]
        self.students_num=students_num
        self.class_num=class_num
        self.class_students_num_region=class_students_num_region

    def expand(self,edit_layer,subject,node_num,solution):
        #这个函数最后要改成所有层所有节点都通用，有待思考
        father_layer_str="layer"+str(edit_layer-1)
        expand_layer_str="layer"+str(edit_layer)
        if self.json["home"][father_layer_str][subject]["children"]==True:
            print "分支失败，请检查"+father_layer_str＋subject+"的children值"
            #这个最后要改成在gui上显示的！！！

        else:
            self.json["home"][father_layer_str][subject]["children"]=True
            node_num_index=[]
            i=1
            while i<=node_num:
                node_num_index.append(i)
                i+=1

            for node in node_num_index:
                self.json["home"][expand_layer_str][subject][node]["children"]=False
                self.json["home"][expand_layer_str][subject][node]["father"]=subject
                self.json["home"][expand_layer_str][subject][node]["num"]=solution[node-1]
                
    def inherit(self,inherit_layer,subject):
        #这个函数是当无法进行expand的时候那么继承父级的数据，以保证层数整齐
        father_layer_str="layer"+str(inherit_layer-1)
        inherit_layer_str="layer"+str(inherit_layer)
        if self.json["home"][father_layer_str][subject]["children"]==True:
            print "继承失败，请检查"+father_layer_str＋subject+"的children值"
            #这个最后要改成在gui上显示的！！！
        else:
            self.json["home"][father_layer_str][subject]["children"]==True
            self.json["home"][inherit_layer][subject]["node1"]["num"]=self.json["home"][father_layer_str][subject]["num"]
            self.json["home"][inherit_layer][subject]["node1"]["children"]=False
            self.json["home"][inherit_layer][subject]["node1"]["father"]=subject

    def edit(self,edit_layer,subject,node_number,edit_key,edit_value):
        #还没想完整，有点奇怪
        pass


    def step1(self):
        # Step 1
        # Search the layer1
        # Which num can be divided into two parts
        for key in self.json["home"]["layer1"].keys():
            
            if self.json["home"]["layer1"][key]["num"]>=40:          
                solution=[]
                node_num=1
                for n in range(1,self.class_num):
                    num=self.json["home"]["layer1"][key]["num"]
                    if self.json["home"]["layer1"][key]["num"]<=n*40:                        
                        num-=40
                        node_num+=1
                        if num=40:
                            solution.append(40)
                        else:
                            solution.append(num)
                self.expand(2,key,node_num,solution)
                #！！！！
            else:
                self.inherit(2,key)

    def show(self):
        for key in self.json["home"][layer1].keys():
            #遍历第一层

            #然后这里要把数据导入到控件里面，待写

            pass
        for key in self.json["home"][layer2].keys():
            #遍历第二层
            #同上
            #待写
            pass

        if self.json["home"][layer_num]>2:
            layer_num=self.json["home"][layer_num]
            layer_index=[]
            i=3
            while i<=layer_num:
                layer_index.append(i)
                i+=1
            for layer in layer_index.keys():
                for subject in self.json["home"][layer].keys():
                    for node in self.json["home"][layer][subject].keys():
                        for num in self.json["home"][layer][subject][node].keys():
                            # 这里最后应该也改成将数据导入到控件
                            print self.json["home"][layer][subject][node][num]
