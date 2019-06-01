class Staff:
    """
    员工类
    """
    def __init__(self,base_salary):
        self.base_salary = base_salary
    def wage(self):
        return self.base_salary

class General_staff(Staff):
    """
    普通员工
    """

    def __init__(self, base_salary, ):
        super().__init__(base_salary)
    def wage(self):
        return self.base_salary
class Programmer(Staff):
    """
    程序员
    """
    def __init__(self,base_salary,project_money):
        super().__init__(base_salary)
        self.project_money = project_money
    def wage(self):
        return super().wage()+self.project_money

class Salesman(Staff):
    """
    销售
    """
    def __init__(self, base_salary, sales_money):
        super().__init__(base_salary)
        self.sales_money = sales_money

    def wage(self):
        return super().wage()+self.sales_money


"""
练习：   老王转岗
    销售----> 程序员
    lw =  Salesmen("老王",3000,500)
    lw  = Programmer("老王",8000,100000)  
    
    重新创建新对象，替换引用，好比是开除“老王”，招聘新“老王”
    要求：对象部分改变,而不是全部改变.
        
"""