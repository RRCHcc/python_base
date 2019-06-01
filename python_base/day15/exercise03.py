"""
练习： 参照下列代码 ：定义 MyRange 类，实现相同效果

"""
# class MyRangerIterator:
#     def __init__(self, targer):
#         self.targer = targer
#         self.inder = 0
#     def __next__(self):
#         if self.inder >= self.targer:
#             raise StopIteration
#         item = self.inder
#         self.inder +=1
#         return item

class MyRange:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        inder = 0
        # return MyRangerIterator(self.number)
        while inder < self.number:
            yield inder
            inder +=1

# for item in range(5):
#     print(item)
t01 = MyRange(5)
for i in t01:
    print(i)

