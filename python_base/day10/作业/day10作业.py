"""
1.  使用面向对象思想,写出下列场景:
    玩家(攻击力)攻击敌人,敌人受伤(血量)后掉血,还可能死亡(播放动画).
    敌人(攻击力)攻击力攻击玩家,玩家(血量)受伤后碎屏,还可能死亡(游戏结束).

程序调试,画出内存图.

"""

class Play:
    def __init__(self, atk=0, hp=0):
        self.atk = atk
        self.hp = hp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self,value):
        self.__atk = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def attker_enemy(self, enemy):
        # enemy.enemy_hp -= self.atk
        print("打死你")
        # 调用敌人受伤方法
        enemy.enemy_hurt(self.atk)
    def play_hurt(self,value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()

    def __death(self):
        print("玩家死亡")

class Enemy:

    def __init__(self,  atk=0, hp=0):

        self.enemy_atk= atk
        self.enemy_hp= hp
    @property
    def enemy_atk(self):
        return self.__enemy_atk
    @enemy_atk.setter
    def enemy_atk(self,value):
        self.__enemy_atk = value
    @property
    def enemy_hp(self):
        return self.__enemy_hp
    @enemy_hp.setter
    def enemy_hp(self, value):
        self.__enemy_hp = value

    def attker_play(self, play):
        print("打死你")
        play.paly_hurt(self.enemy_atk)

    def enemy_hurt(self,value):
        self.enemy_hp -= value
        if self.enemy_hp <= 0:
            self.__death()

    def __death(self):
        print("死啦,播放动画")


p01 = Play(100,10000)
e01 = Enemy(10,2000)
# while e01.enemy_hp > 0 or p01.hp > 0:
#     p01.attker_enemy(e01)
    # e01.attker_play(p01)

p01.attker_enemy(e01)