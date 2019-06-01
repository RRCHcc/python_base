"""


"""

class Student:
    """
        学生
    """
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def learning(self):
        print(self.name+"学习")
    def work(self):
        print(str(self.age)+"工作")
        #s01 悟空对象的地址
studeng01 =Student("悟空",19)

studeng02 =Student("八戒",20)

#通过对象地址，使用对象方法，会自动传递对象地址
studeng01.learning()
studeng02.work()

studeng01 =Student("悟空",19)

