"""
练习：重写StudentModel类 __str__ 方法与__repr__


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
    def __str__(self):#给人卡看
        return '你好,我叫"%s"今年%d,考试成绩是%f,编号为%d'%(self.name,self.age,self.score,self.id)
    def __repr__(self):#给机器看，可以克隆一个
        return 'StudentModel("%s",%d,%d,%d)'%(self.name,self.age,self.score,self.id)

s01 = StudentModel("zs",18,99)
s02 = StudentModel("ff",19,88)
list01=[]
# print(s01)
# print(s02)
list01.append(s01)
list01.append(s02)
# print(list01)
s03 =eval(s01.__repr__())
s01.name = "pp"
print(s01)
# print(s03)











