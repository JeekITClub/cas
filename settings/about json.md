#JSON 说明文档#
##JSON##
key:value<br>
key必须是"字符串"<br>

##teachers.json##
	"teachersNum": 2
teachersNum 为教师总数量

	    "1": {
    "num": "1",
    "name": "A",
    "subject": "Physics",
    "grade_layer": {
      "grade1A": true,
      "grade1B": true,
      "grade2A": false,
      "grade2B": false,
      "grade3A": false,
      "grade3B": false
    },
    "teach":true
  	
"1"为索引，可以理解成编号1<br>
num 编号<br>
name 名字<br>
subject 所教科目<br>
grade_layer 是指教哪个年级哪个分层 用true和false<br>
数学语文英语 年级+B/C<br>
物化生史地政 年级+A/B<br>
体育没有分<br>
音乐，心理等没分<br>

##students.json##
studentsNum 学生总数<br>
"20150101" 学生的索引<br>
num 学号<br>
name 名字<br>
pclass 行政班<br>
tclass 教学班<br>


##classroom.json##
pclassroom 行政班数量<br>
tclass 是教学班
PhysicsB1 指的是物理B1班在哪个行政班 比如等于1 那么就是物理B1班上课就是在行政1班

##settings.json##
后续补充需要设置的各项内容