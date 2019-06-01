"""
１．创建技能类(编号，技能名称，冷却时间，攻击力，消耗法力)
　　创建技能列表．
　　－－　定义函数：查找编号是１０１的技能对象
　　－－　定义函数：查找冷却时间为０的所有技能对象
　　－－　定义函数：查找攻击力大于５的所有技能对象
　　－－　定义函数：查找攻击力大于１０，并且不需要消耗法力的所有技能．

"""
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
    Skill(101,"降龙十八掌", 15, 80, 30),
    Skill(102,"佛山无影脚", 12, 60, 20),
    Skill(103,"还我漂漂拳", 0, 15, 5),
    Skill(104,"呵呵哈哈哈或", 1, 3, 0),
    Skill(105,"上山打老虎", 0, 12, 3)
]
#将以下代码，不变的部分提取到一个方法  find_all()
#将变化点，提取到不同方法
#实现原有功能
#相同点
# def find_all(target,func):
#     for item in target:
#         if func(item):
#             yield item
from common.custom_list_helper import ListHelper
#不同点
def find_id(item):
    return item.id == 101
def find_cd(item):
    return item.cd == 0
def find_atk(item):
    return item.atk > 5
def find_atk_mp(item):
    return item.atk > 10 and item.mp == 0

for item in ListHelper.find_all(list,lambda item:item.id == 101):
# for item in find_all(list,find_id):
    print(item)
for item in ListHelper.find_all(list, lambda item:item.cd == 0):
    print(item)
for item in ListHelper.find_all(list, lambda item:item.atk > 5):
    print(item)
for item in ListHelper.find_all(list, lambda item:item.atk > 10 and item.mp == 0):
    print(item)




    
# for item in find_all(list, find_cd):
# def find_id(target,value):
#     for item in target:
#         if item.id == value:
#             yield item
# def find_cd(target):
#     for item in target:
#         if item.cd == 0:
#             yield item
# def find_atk(target):
#     for item in target:
#         if item.atk > 5:
#             yield item
# def find_atk_zero_mp(target):
#     for item in target:
#         if item.atk > 10 and item.mp == 0:
#             yield item


















