"""
练习： 在list01当中，挑出所有偶数
要求使用1)生成器函数

"""

list01 = [23, 3, 4, 556, 677, 68, 8, 98, 98]

def even_number(list01):

    for item in list01:
        if item %2 ==0:
            yield item

l01 = even_number(list01)
for i in l01:
    print(i)
