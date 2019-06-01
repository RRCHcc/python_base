"""
练习：    选出所有女同学
        要求使用生成器函数实现
"""
class Student:
    def __init__(self, name, sex, age, score):
        self.name = name
        self.sex = sex
        self.age = age
        self.score = score
    def __str__(self):
        return "%s--%s--%d--%d"%(self.name,self.sex,self.age,self.score
                                 )
list_stu = [
            Student("张无忌", "男", 28, 82),
            Student("赵敏", "女", 25, 95),
            Student("周芷若", "女", 26, 88)
]

def get_girl(target):
    for item in target:
        if item.sex == "女":
            yield item


for i in get_girl(list_stu):
    print(i)