"""
1. 定义父类:武器,数据:攻击力,  行为:购买(所有子类都一样). 攻击(不知道怎么攻击)
   定义子类:枪,数据:射速,     行为:攻击
   定义子类:手雷,数据:爆炸范围,行为:攻击
   创建相应对象,调用相应方法.
   画出内存图
"""



class Weapons:
    """
    武器
    """
    def __init__(self, atk):
        self.atk = atk

    def buy(self):
        print("购买武器")
    def attack(self):
        raise NotImplementedError()
class Gun(Weapons):
    """
    枪
    """

    def __init__(self, atk,atk_speed):
        super().__init__(atk)
        self.atk_speed = atk_speed

    def attack(self):
        print("开枪啦")
class Grenades(Weapons):
    """
    手雷
    """
    def __init__(self, atk, blow_range):
        super().__init__(atk)
        self.blow_range =blow_range
    def attack(self):
        print("爆炸啦")


g01 = Gun(10,0.1)
g01.buy()