"""
练习：     手雷爆炸了,可能伤害敌人,玩家.
          还有可能伤害未知事物（鸭子,树....）,
    要求： 如果增加了新的事物,手雷代码不变.

"""
class Hand_grenades:
    """
    手雷
    """
    def __init__(self, name, atk=0 ):
        self.name = name
        self.atk = atk
    def attack(self, *args):
        for item in args:
            if not isinstance(item, Injured):
                print("你不是我儿子，我打儿子呢")
                return
            item.injured(self.atk)
class Injured:
    def __init__(self, hp):
        self.hp = hp
    def injured(self,value):
        #约束子类，必须具有当前方法
        # raise NotImplementedError()
        self.hp -= value
class Player(Injured):
    def injured(self,value):
        super().injured(value)
        print("啊，我受伤啦")

class Enemy(Injured):
    def injured(self,value):
        super().injured(value)
        print("我擦,电脑这边的也打")

p01 = Player(100)
e01 = Enemy(50)
h01 = Hand_grenades(50)

h01.attack(p01)
h01.attack(e01, p01)
