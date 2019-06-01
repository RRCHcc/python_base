"""
界面 表示层
"""
from bll import StudentManagerController
from model import StudentModel

class StudentManagerView:
    """
    界面视图类
    """
    def __init__(self):
        #创建逻辑控制器对象
        self.__manager = StudentManagerController()
    def __input_int(self,str):
        while True:
            try:
                return int(input(str))
            except:
                print("输入有误")

    def __input_student(self):#1
        #1,在控制台中录入学生信息,存成学生对象StudentModel
        #2,调用逻辑控制器的add_student方法
        stu = StudentModel()
        stu.name = input("请输入学生姓名")
        # stu.age = int(input("请输入学生年龄"))
        stu.age = self.__input_int("请输入学生年龄")
        # stu.score = float(input("请输入学生成绩"))
        stu.score = self.__input_int("请输入学生成绩")
        self.__manager.add_student(stu)
        # print(self.__manager)
    def __output_students(self,list_target):#2
        """
            显示学生
        :return: 学生信息
        """
        # for item in self.__manager.stu_list:
        for item in list_target:
            print(item.id, item.name, item.age, item.score)
    def __delete_student(self):#3
        # value = int(input("请输入需要删除的学生id"))
        value = self.__input_int("请输入需要删除的学生id")
        if self.__manager.remove_student(value):
            print("删除成功")
        else:
            print("删除失败")
    def __modify_student(self):#4
        """
        修改学生信息
        :return:
        """
        stu = StudentModel()
        # stu.id = int(input("请输入需要修改的学生id"))
        stu.id = self.__input_int("请输入需要删除的学生id")
        stu.name = input("请输入学生姓名")
        # stu.age = int(input("请输入学生年龄"))
        stu.age =self.__input_int("请输入学生年龄")
        # stu.score = float(input("请输入学生成绩"))
        stu.score = self.__input_int("请输入学生成绩")
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):#5
        """
        根据成绩排序
        :return:
        """
        list_target = self.__manager.sorting_stu_by_score()
        self.__output_students(list_target)


    def __display_menu(self):
        """
        显示菜单
        :return:
        """

        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩降序排列")

    def __select_menu(self):
        number = input("请输入选项：")
        if number == "1":
            self.__input_student()
        elif number == "2":
            self.__output_students(self.__manager.stu_list)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            self.__output_student_by_score()
    def main(self):
        """
        界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

