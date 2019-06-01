"""
        练习 ： 定义敌人类（姓名，攻击力，攻击速度0---10，血量0----100）
        用两个方法将数据保护起来
"""
class Enemy:
    def __init__(self,name, atk=0, atk_spend=0, hp=0):
        self.set_name(name)
        self.set_atk(atk)
        self.set_atk_spend(atk_spend)
        self.set_hp(hp)
    def get_name(self):
        return self.__name
    def set_name(self,value):
        self.__name =value
    def get_atk(self):
        return self.__atk
    def set_atk(self,value):
        self.__atk = value
    def get_atk_spend(self):
        return self.__atk_spend
    def set_atk_spend(self,value):
        if 0 <= value <=10:
            self.__atk_spend = value
        else:
            self.__atk_spend = 0
            print("速度超过范围")
    def get_hp(self):
        return self.__hp

    def set_hp(self,value):
        if 0 <= value <=100:
            self.__hp = value
        else:
            self.__hp = 0
            print("血量超过范围")

re = Enemy("ZS",200,50,200)
print(re.get_name(),re.get_hp(),re.get_atk_spend(),re.get_atk())


