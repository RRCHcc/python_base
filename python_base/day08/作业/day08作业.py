"""
１． 发散性试题：
    以"万物皆对象"思想，洞察身边的事物，
    创建２个类，２个对象．

"""
class Clohes:
    """
    衣服
    """
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def print_self(self):
        print(self.name,self.color)
class Phone:
    """
    手机
    """
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def print_self(self):
        print(self.brand,self.color)

c01=Clohes("AD","红色")
c01.print_self()
p01=Phone("iphone","黑色")
p01.print_self()