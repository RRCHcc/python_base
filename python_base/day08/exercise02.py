"""
    练习：
"""

class Enemy:
    """
    敌人
    """
    def __init__(self,name="",hp=0.0,atk=0,atk_spend=0.0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_spend =atk_spend

    def print_self(self):
        print(self.name,self.hp,self.atk,self.atk_spend)

    @staticmethod
    def find_enemy(find_name, list01):
        # 遍历敌人列表
        for item in list01:
            # 如果有指定名称的敌人对象
            if item.name == find_name:
                # 则返回对象地址
                return item
#1,在控制台中输入3个敌人，存入列表
#2,将敌人列表输出（调用print_self）到控制台
#类 可以包装 多个数据
list01 = []
for i in range(2):
    e = Enemy()
    e.name = input("请输入敌人姓名：")
    e.hp = int(input("请输入敌人血量"))
    e.atk = float(input("请输入敌人攻击力："))
    e.atk_spend = int(input("请输入敌人攻击速度："))
    e.print_self()
    list01.append(e)
for item in list01:
    item.print_self()

#  练习：  定义函数，在敌人列表中，根据姓名查找敌人对象
e01 = Enemy("zs",)


re =Enemy.find_enemy("zz",list01)
if re != None:
    re.print_self()
else:
    print("没有找到")






