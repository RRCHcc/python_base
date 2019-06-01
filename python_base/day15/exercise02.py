"""
员工管理器
"""
class Employee:
    pass

# class  EmployeeIterator:
#     def __init__(self, targer):
#         self.targer = targer
#         self.inder = 0
#     def __next__(self):
#         if self.inder > len(self.targer)-1:
#             raise StopIteration
#         item = self.targer[self.inder]
#         self.inder +=1
#         return item

class EmployeeManager:
    def __init__(self,employees):
        self.all_employee = employees
    def __iter__(self):
        # return EmployeeIterator(self.all_employee)
        for item in self.all_employee:
            yield item

manager = EmployeeManager([Employee(),Employee()])
# for item in manager:
#     print(item)
iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except Exception as e:
        print(e)
        break


