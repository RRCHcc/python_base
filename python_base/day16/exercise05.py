"""
练习：
    解决的问题：
        查找编号是101的（单个）技能对象
        查找 cd 大于10的（单个）技能对象
        查找 姓名“降龙十八掌” 的（单个）技能对象
"""
from common.custom_list_helper import ListHelper
class Skill():
    def __init__(self,id,name,cd,atk,mp):
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

i =ListHelper.find_first(list,lambda item:item.id == 101)
print(i)
i = ListHelper.find_first(list, lambda item: item.cd >10)
print(i)
i = ListHelper.find_first(list, lambda item: item.name == "降龙十八掌")
print(i)