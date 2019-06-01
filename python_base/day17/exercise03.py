"""
解决问题：
        根据指定条件升序排列列表
        按照血量升序排列
        按照攻击力升序排列
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
# def ascending(target):
#     for i in range(len(target)-1):
#         for item in range(i,len(target)):
#             if target[i].hp> target[item].hp:
#                 target[i],target[item]=target[item],target[i]
ListHelper.ascending(list,lambda item:item.hp)
for i in list:
    print(i)
print("-----------")
ListHelper.ascending(list,lambda item: item.atk)
for i in list:
    print(i)


