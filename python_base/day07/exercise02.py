"""
练习：
统计一个方法的调用次数
"""
count = 0
def fun01():

    global count
    count +=1
    pass

print(fun01())
print(fun01())
print(fun01())
print(fun01())
print(count)