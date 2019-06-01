"""
练习1： （“悟空",”八戒“,”沙僧“,”唐僧“）
    使用while +迭代器 获取元组所有元素
练习2：{”张三丰“：101,”张无忌“：102,”赵敏“：102}
    不使用for循环，获取字典所有元素

"""

tuple01 = ("悟空", "八戒", "沙僧", "唐僧")
#1.获取迭代器对象
iterator = tuple01.__iter__()
while True:
    try:
        #2.获取下一个元素（迭代过程
        item = iterator.__next__()
        print(item)
        #3.停止迭代（捕获异常）
    except StopIteration:
        break


dict01 = {"张三丰": 101, "张无忌": 102, "赵敏": 102}
iterator01 = dict01.__iter__()
while True:
    try:
        item = iterator01.__next__()
        print(item, dict01[item])
    except StopIteration:
        break
