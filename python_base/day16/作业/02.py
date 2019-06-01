"""
目标２：可以在实际项目中，灵活运用函数式编程思想．
解决的问题：获取满足条件的最后一个对象
                最后一个活人
                攻击速度大于５的最后一个敌人

解决的问题：获取满足条件的对象总数
                  具有生命值的对象总数
                  攻击速度小于２０的敌人总数

解决的问题：判断列表中是否包含某个元素
                列表中是否具有死人
                列表中是否具有攻击速度大于１０的敌人

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
        return "%d--%s--%d--%d--%d"%(
            self.id,self.name,self.atk,self.hp,self.atk_speed
        )

list = [
        Enemy(101,"哇哈哈", 4, 0, 1),
        Enemy(102,"李连杰替身", 18, 60, 17),
        Enemy(103,"功夫小胖", 21, 55, 29),
        Enemy(104,"张三李四", 12, 30, 5),
        Enemy(105,"什么鬼", 3, 10, 1)
]

# def find_last(target):
#     for item in range(len(target)-1,-1,-1):
#         if item.hp> 0:
#
#     return target[item]
# print(find_last(list))
#1
# --------1)
print(ListHelper.find_last_demo(list, lambda item: item.hp > 0))
# --------2)
print(ListHelper.find_last_demo(list, lambda item: item.atk_speed > 5))
#2
# #---------1)
# print(ListHelper.total(list,lambda item:item.hp > 0))
# #---------2)
# print(ListHelper.total(list,lambda item:item.atk_speed>20))
# #3
# #--------1)
# print(ListHelper.judge(list,lambda item:item.hp==0))
# #--------2)
# print(ListHelper.judge(list,lambda item:item.atk_speed>10))



