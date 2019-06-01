"""

"""
class Wife:
    """
        老婆
    """
    #1，数据成员：姓名，年龄，性别...

    def __init__(self,name,age,sex):
        # self 字面意思就是自己，调用当前方法的对象
        # 就是我们创建的对象地址
        print(id(self))
        self.name = name
        self.age = age
        self.sex = sex
    #2，方法成员：做饭...
    def cooking(self):
        print("做饭")

#创建对象（实例化）
#调用__init__(self,name,age,sex)方法
w01 = Wife("丽丽",20,"女")
print(id(w01))
#调用对象的方法
w01.cooking()

#在内存中，方法有一个，对象有多份















