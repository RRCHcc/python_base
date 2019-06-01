"""
准备：
　　－－　创建敌人类（编号／姓名／攻击力／血量／攻击速度．．．）
　　－－　创建敌人列表
练习：
　　 1. 查找所有死人.
    2. 查找编号是101的敌人
    3. 查找所有活人.
    4. 计算所有敌人攻击力总和
    5. 查找所有攻击速度在５－－１０之间的敌人
    6. 查找所有敌人的姓名
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
        Enemy(105,"什么鬼", 3, 0, 1)
]
#1--------
for item in ListHelper.find_all(list,lambda item:item.hp==0):
    print(item)
#2----------
print(ListHelper.find_first(list,lambda item: item.id == 101))
#3-----------
for item in ListHelper.find_all(list,lambda item :item.hp >0):
    print(item)
#4-----------
print(ListHelper.sum(list,lambda item:item.atk))
#5---------
for item in ListHelper.find_all(list,lambda item:5<=item.atk_speed<=10):
    print(item)
#6------------
for item in ListHelper.select(list,lambda item:item.name):
    print(item)