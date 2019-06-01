"""
2. 一家公司,有如下几种岗位:
    普通员工:底薪
    程序员:底薪 + 项目分红
    销售员:底薪 + 销售额
   定义员工管理器,记录所有员工,提供计算总薪资方法.
   要求:增加新岗位,员工管理器代码不做修改.
   体会:依赖倒置
"""
class EmployeesManager:
    """
    员工管理器
    """
    def __init__(self):
        self.__employees_list = []
    def get_employees(self,g):
        if not isinstance(g,Staff):
            return
        self.__employees_list.append(g)
    def total_wages(self):
        total_wages = 0
        for item in self.__employees_list:
            total_wages += item.wage()
        return total_wages

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

em01 =EmployeesManager()

g01 = General_staff(2030)
p01 = Programmer(7000,10000)
s01 = Salesman(2030,8000)
em01.get_employees(g01)
em01.get_employees(p01)
em01.get_employees(s01)
print(em01.total_wages())

