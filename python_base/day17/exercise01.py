"""
    练习：
     解决问题：删除所有死人
             删除编号是101的敌人
             删除攻击力小于5的敌人
             倒着删除
"""
from common.custom_list_helper import ListHelper
class Enemy():
    def __init__(self,id,name,atk,hp,atk_speed):
        self.id = id
        self.name = name
        self.atk = atk
        self.hp = hp
        self.atk_speed = atk_speed
    def __str__(self):
        return "%d--%s--%d--%d--%d"%(self.id,self.name,self.atk,self.hp,self.atk_speed)

list = [
        Enemy(101,"哇哈哈", 4, 0, 1),
        Enemy(102,"李连杰替身", 18, 60, 7),
        Enemy(103,"功夫小胖", 21, 55, 9),
        Enemy(104,"张三李四", 12, 30, 5),
        Enemy(105,"什么鬼", 300, 10, 1)
]
# def delete(target,func_conditation):
#     for item in range(len(target)-1,-1,-1):
#         if target[item].hp == 0:
#             target.remove(target[item])
#             return target
# print(ListHelper.delete(list,lambda item: item.hp == 0))
# print("---------")
# print(ListHelper.delete(list, lambda item: item.id == 101))
# print("---------")
# print(ListHelper.delete(list, lambda item: item.atk > 5))
"""
练习：
    解决问题：获取满足条件的最大值
    获取血量最大的敌人
    获取攻击力最强的
"""
def find_max(target):
    max_number=target[0]
    for item in range(1,len(target)):
        if max_number.atk <target[item].atk:
            max_number = target[item]
    return max_number
#
# print(find_max(list))
re01=ListHelper.find_max(list,lambda item:item.hp)
print(re01)
re02=ListHelper.find_max(list,lambda item:item.atk)
print(re02)
