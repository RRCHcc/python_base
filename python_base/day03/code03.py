"""
循环语句
    -----for

"""

#for 变量列表 in 可迭代对象
#   语句
# for element in "我爱你":
#     print(element)

#rang（）函数，整数生成器
#熟练正 倒 跳 生成数字

# for element in range(1,5,1):# 输出结果：1,2,3,4
#     print(element)
#
# for element in range(1,6,2):#输出结果：1,3,5
#     print(element)
#
for element in range(5,-1,-1):#输出结果：5 4 3 2 1 0
    print(element)

#for 循环比while ，更适合做预定次数的循环