"""
解决的问题１：
　　　获取敌人列表中，攻击力最小的敌人．
　　　使用内置高阶函数和ListHelper实现．

解决的问题２：
　　　根据血量对敌人列表进行降叙排列
　　　使用内置高阶函数和ListHelper实现．

在ListHelper中，定义万能(任意条件／升序／降序)排序方法．
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
        Enemy(101, "哇哈哈哈哈hahahah", 4, 0, 1),
        Enemy(102, "李连杰替身", 18, 60, 7),
        Enemy(103, "功夫小胖胖", 21, 55, 9),
        Enemy(104, "张三李四无", 12, 30, 5),
        Enemy(105, "什么鬼东西啊", 300, 10, 1)
]
re01=min(list,key= lambda e:e.atk)
print(re01)
# def find_min(target,func_condition):
#     min = target[0]
#     for item in range(1,len(target)):
#         if func_condition(min) >func_condition(target[item]):
#             min = target[item]
#     return min
re02 = ListHelper.find_min(list,lambda e:e.atk)
print(re02)
#---------
"""
解决的问题２：
　　　根据血量对敌人列表进行降叙排列
　　　使用内置高阶函数和ListHelper实现．
"""
re03 = sorted(list,key=lambda e: e.hp,reverse = True)
for i in re03:
    print(i)
print("----------------")
ListHelper.order_by_descending(list,lambda e: e.hp)
for item in list:
    print(item)

print("----------------")
#面试题：自定义排序方法，实现对列表的升序排列
    #在ListHelper中，定义万能(任意条件／升序／降序)排序方法．
def order_down(target,func_condition,):
    for i in range(len(target) - 1):
        for r in range(i + 1, len(target)):
            if func_condition(target[i],target[r]):
                target[i], target[r] = target[r], target[i]

order_down(list,lambda e01,e02:e01.hp<e02.hp)
for i in list:
    print(i)