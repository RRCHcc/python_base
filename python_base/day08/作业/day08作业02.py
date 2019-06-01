"""
２. 创建学生类
    －－　数据：姓名，性别，年龄，成绩．
    －－　行为：print_self()
   画出学生列表内存图
   定义函数：
        －－　定义函数，在学生列表中，根据姓名查找学生对象．
        －－　定义函数，在学生列表中，根据性别查找所有学生对象．
        －－　查找年龄大于20，成绩大于60的所有学生对象．

"""
class Student:
    def __init__(self,name="", sex="", age=0, grade=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade
    def print_self(self):
        print(self.name,self.sex,self.age,self.grade)
list01 = []
for i in range(5):
    student = Student()
    student.name = input("请输入学生姓名：")
    student.sex = input("请输入学生性别：")
    student.age = int(input("请输入学生年龄："))
    student.grade = float(input("请输入学生成绩："))
    student.print_self()
    list01.append(student)
for item in list01:
    item.print_self()


def find_student(find_name,list01):
    for i in list01:
        if i.name == find_name:
            return i

re = find_student("zz",list01)
if re not in list01:
    print("没有找到")
else:
    re.print_self()
def in_sex_find_student(find_sex,list01):
    #使用列表存储多个结果
    the_same_list = []
    for i in list01:
        if i.sex == find_sex:
            the_same_list.append(i)
            return the_same_list

s01 = in_sex_find_student("女",list01)
for i in s01:
    i.print_self()

#查找年龄大于20，成绩大于60的所有学生对象．
list02 = []
for c in list01:
    if c.age >20 and c.grade>60:
        list02.append(c)
        break
for cc in list02:
    cc.print_self()





