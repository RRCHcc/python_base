"""
练习：
    定义父类 ----> 宠物，行为：吃
                      数据：名字
    定义子类----> 狗,行为： 看家
                      数据：工作
    定义子类----> 鸟,行为：

    创建相应对象，调用相应方法，使用isinstance，issubclass函数
"""
class Pet:
    def __init__(self, name):
        self.name = name

    def eating(self):
        print("吃")

class Dog(Pet):
    def __init__(self, name, work):
        super().__init__(name)
        self.work = work

    def watch_home(self):
        print("汪汪汪")

class Bird(Pet):

    def flying(self):
        print("飞")

d01 = Dog("元宝", "逗利是")
b01 = Bird("会飞")
p01 = Pet("油腻腻")
print(d01.name, d01.work)
print(b01.name)
print(p01.name)
d01.watch_home()
d01.eating()
b01.flying()
b01.eating()
p01.eating()
print(issubclass(Dog, Pet))
print(issubclass(Bird, Pet))
print(issubclass(Bird, Dog))
print(issubclass(Pet, object))
print(isinstance(d01, Pet))
print(isinstance(d01, Bird))
print(isinstance(p01, Pet))
print(isinstance(b01, Pet))
print(isinstance(d01,(Pet, Dog)))
print(isinstance(d01,(Bird, Dog)))
print(isinstance(b01,(Pet, Dog)))
