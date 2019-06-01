"""
    解决问题： 求和 sum
        技能列表---> 所有技能编号的和

"""
from common.custom_list_helper import ListHelper

class Skill():
    def __init__(self, id, name, cd, atk, mp):
        self.id = id
        self.name = name
        self.cd =cd
        self.atk =atk
        self.mp =mp

    def __str__(self):
        return "%d--%s--%d--%d--%d"%(self.id,self.name,self.cd,self.atk,self.mp
                                     )
list = [
    Skill(100,"降龙十八掌", 15, 80, 30),
    Skill(101,"佛山无影脚", 12, 60, 20),
    Skill(103,"还我漂漂拳", 0, 15, 5),
    Skill(104,"呵呵哈哈哈或", 1, 3, 0),
    Skill(105,"上山打老虎", 0, 12, 3)
]
a01=ListHelper.sum(list,lambda item: item.cd)
print(a01)

