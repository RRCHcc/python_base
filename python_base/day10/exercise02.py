"""
        练习：小明在招商银行取钱

"""
class Person():
    def __init__(self, name, money=0):
        self.name = name
        self.money = money


class Bank():
    def __init__(self,name,money):
        self.name = name
        self.total_money = money
       #考虑：取钱逻辑，应该有银行决定，所以取钱方法，定义在银行
    def draw_money(self,person,value):
        if self.total_money >=value:
            self.total_money -=value
            person.money +=value
            print("取钱成功")
        else:
            print("取钱失败")

p01=Person("小明")
b02 = Bank("招商银行", 1000000)
b02.draw_money(p01, 5000000)


