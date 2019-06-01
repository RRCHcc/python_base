"""
业务逻辑层
"""

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
