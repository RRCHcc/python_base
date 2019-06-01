"""
2. 以面向对象的思想，描述下列场景.
    提示：对象与对象数据不同，类与类行为不同．
　　张三　教　李四　学习python
   李四  教 张三　 玩游戏
   张三　工作　挣了８０００元
   李四　工作　挣了３０００元
"""
class Object:
    def __init__(self, name):
        self.name = name
        self.__skills = []
        self.__total_money = 0
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name = value
    @property
    def skills(self):#只读不写
        # return  self.__skills #返回可变对象地址，意味着类外任然可以操作可变对象
        return  self.__skills[:]#返回新的可变对象地址，意味着类对外操作新的可变对象，对元对象不改变
        #备注每次通过切片返回新对象，都会另外开辟空间创建新对象，占用过多内存
    @property
    def total_money(self):
        return self.__total_money

    def teach(self, person_other, str_skill):
        person_other.__skills.append(str_skill)
        print(self.__name, "教了",person_other.name,str_skill)

    def work(self,money):
        self.__total_money += money
        print(self.name,"工作赚了",money,"元")
zs = Object("zs")
ls = Object("ls")
zs.teach(ls, "python")
ls.teach(zs,"玩游戏")
zs.work(8000)
ls.work(3000)