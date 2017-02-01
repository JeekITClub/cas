# Package for teacher management
class teacher:
    num = 0
    # 防止教师重名，因此num作为index
    name = ""
    subject = ""
    grade_layer = []
    # 部分教师跨年级上课
    teach = True

    # 部分教师长期病假或产假无法进行正常教学

    def __init__(self):
        pass

    def add_teacher(self, name, subject, grade_layer):
        self.name = name
        self.subject = subject
        self.grade_layer = grade_layer

        pass

    def delete_teacher(self, name, num):
        self.name = name
        self.num = num
        pass

    def edit_teacher(self, name, num, grade_layer, teach):
        # Edit teacher information
        pass
