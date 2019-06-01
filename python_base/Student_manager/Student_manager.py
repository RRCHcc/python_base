"""
学生管理系统
定义学生数据模型类，
创建逻辑控制类，
定义学生列表

"""
class StudentModel():
    """
    学生数据模型类
    """
    def __init__(self, name="", age= 0, score= 0, id= 0):
        """
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score =score

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        self.__score = value


class StudentManagerController:
    """
    学生逻辑控制器
    """
    def __init__(self):
        self.__stu_list =[]
    @property
    def stu_list(self):
        return self.__stu_list


    def add_student(self,student):

        """
        添加新学生
        :param student: 需要添加的学生
        :return:
        """

        student.id = self.__generate_id()
        self.__stu_list.append(student)
    def sorting_stu_by_score(self):
        """
        根据成绩升序排列
        :return:
        """
        list_sorting = self.stu_list[:] #创建新列表（目的：不影响原列表）
        for item in range(len(list_sorting)-1):
            for i in range(item+1,len(list_sorting)):
                if list_sorting[item].score > list_sorting[i].score:
                    list_sorting[item],list_sorting[i]=list_sorting[i],list_sorting[item]
        return list_sorting
    def __generate_id(self):
        # 生成编号的需求:新编号,比上次添加的对象编号多1.
        if len(self.stu_list) > 0:
            id = self.__stu_list[-1].id + 1
        else:
            id = 1
        return id

    def remove_student(self, id):
        for item in self.stu_list:
            if item.id == id:
                self.stu_list.remove(item)
                return True#表示删除成功
            return False   #表示删除失败

    def update_student(self,stu):
        """
        更新学生信息
        :param stu:
        :return:
        """
        for item in self.__stu_list:
            if item.id == stu.id:
                item.name = stu.name
                item.age = stu.age
                item.score = stu.score
                return True
        return False


# controller = StudentManagerController()
# controller.add_student(StudentModel("zs",18, 85))
# controller.add_student(StudentModel("zs",18, 85))
# for i in controller.stu_list:
#     print(i.id, i.name, i.age, i.score)



class StudentManagerView:
    """
    界面视图类
    """
    def __init__(self):
        #创建逻辑控制器对象
        self.__manager = StudentManagerController()

    def __input_student(self):#1
        #1,在控制台中录入学生信息,存成学生对象StudentModel
        #2,调用逻辑控制器的add_student方法
        stu = StudentModel()
        stu.name = input("请输入学生姓名")
        stu.age = int(input("请输入学生年龄"))
        stu.score = float(input("请输入学生成绩"))
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
        value = int(input("请输入需要删除的学生id"))
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
        stu.id = int(input("请输入需要修改的学生id"))
        stu.name = input("请输入学生姓名")
        stu.age = int(input("请输入学生年龄"))
        stu.score = float(input("请输入学生成绩"))
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






















