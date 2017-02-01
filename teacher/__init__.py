#Package for teacher management
class teacher:
    num=0
    #防止教师重名，因此num作为index
    name=""
    subject=""
    grade=[]
    #部分教师跨年级上课
    layer=[]
    #有些老师教两个层次的学生
    teach=True
    #部分教师长期病假或产假无法进行正常教学

    def __init__(self):
        pass
    def add_teacher(self,name,subject,grade):

        self.name=name
        self.subject=grade
        self.grade=grade

        pass
    def delete_teacher(self,name,num):
        self.name=name
        self.num=num
        pass
    def edit_teacher(self,name,num,teach):
        #Edit teacher information
        pass