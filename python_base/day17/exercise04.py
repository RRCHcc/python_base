"""
练习：
    要求使用内置函数
    查找：1）血量在10---50之间的所有敌人
         2）所有敌人的攻击力和血量
         3）根据敌人攻击力列表进行升序排列
         4）姓名字数最长的敌人
"""

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
#1)
for item in filter(lambda e:10<=e.hp<=50,list):
    print(item)
#2)
print("--------")
for item in map(lambda e:(e.atk,e.hp),list):
    print(item)
#3)
print("--------")
for item in sorted(list,key=lambda e:e.atk):
    print(item)
#4)
print("--------")
re01=max(list,key=lambda e:len(e.name))
print(re01)