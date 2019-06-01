"""
练习：对象计数器
    创建老婆类（名字...），随意实例化对象
    统计老婆数量（定义方法
    画出内存图
"""
class Wife:
    """
    老婆
    """
    count = 0

    @classmethod
    def print_wife_count(cls):
        return Wife.count
    def __init__(self,name,age,higt):
        #实例变量
        self.name = name
        self.age = age
        self.higt =higt
        #统计数量
        Wife.count +=1




wo1 = Wife("qq",25,170)
w02 = Wife("ww",22,165)
w03 = Wife("wp",26,168)
#通过类名访问类方法
print(Wife.print_wife_count())