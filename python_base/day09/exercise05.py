"""
        练习 ： 修改定义敌人类（姓名，攻击力，攻击速度0---10，血量0----100）
        用属性将数据保护起来
"""
class Enemy:
    def __init__(self,name, atk=0, atk_spend=0, hp=0):
        self.name = name
        self.atk = atk
        self.atk_spend = atk_spend
        self.hp = hp
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        self.__name =value

    @property
    def atk(self):
        return self.__atk
    @atk.setter
    def atk(self,value):
        self.__atk = value

    @property
    def atk_spend(self):
        return self.__atk_spend
    @atk_spend.setter
    def atk_spend(self,value):
        if 0 <= value <=10:
            self.__atk_spend = value
        else:
            self.__atk_spend = 0
            print("速度超过范围")
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self,value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            self.__hp = 0
            print("血量超过范围")

re = Enemy("ZS",200,5,50)
print(re.name)
print(re.atk)
print(re.atk_spend)
print(re.hp)


