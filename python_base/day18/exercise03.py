"""
为学生的学习方法添加新功能（统计执行时间）
记录时间
"""
import time
def statistical_time(func):

    def wrapper(*args,**kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        time_execute =time.time()-time_start
        print("执行时间是：",time_execute)
        return result
    return wrapper

class Student:
    def __init__(self,name):
        self.name = name

    @statistical_time
    def stay(self):
        print("开始学习了")
        time.sleep(5)#睡眠两秒，模拟学习了两秒


s01 = Student("zs")
s01.stay()
