"""
练习：
    解决问题：获取满足条件的最大值
    获取血量最大的敌人
    获取攻击力最强的
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
        Enemy(101, "哇哈哈哈哈", 4, 0, 1),
        Enemy(102, "李连杰替身", 18, 60, 7),
        Enemy(103, "功夫小胖胖", 21, 55, 9),
        Enemy(104, "张三李四无", 12, 30, 5),
        Enemy(105, "什么鬼东西", 300, 10, 1)
]
re01=ListHelper.find_max(list,lambda item:item.hp)
print(re01)
re02=ListHelper.find_max(list,lambda item:item.atk)
print(re02)

