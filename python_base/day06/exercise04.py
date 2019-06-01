"""
    列表是否具有相同元素
    [1,4,7,4,8,0,6]
    核心：所有元素间两两比较
    思想： 取出第一个元素，与后面进行比较
            取出第二个元素，与后面进行比较
"""
state = False# 假设没有相同元素
list01 = [1, 4, 7, 4, 8, 0, 6]
#取出几个元素
for r in range(len(list01)-1):
    #与后面的元素进行比较
    for c in range(r + 1, len(list01)):
        #如果发现相同元素
        if list01[r] == list01[c]:

            state = True
            break# 退出就近循环体(退出内层循环
    if state:
        break#退出外层循环
if state:
    print("有重复")
else:
    print("没有")

