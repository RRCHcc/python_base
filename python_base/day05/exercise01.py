"""
练习：
使用range生成1--10之间的数字，存入列表list01中
使用列表推导式，将list01中所有奇数存入list02
              将list01中所有偶数存入list03
              将list01中元素大于3的存入list04

"""
list01 = [i for i in range(1,11)]

list02 = [i for i in list01 if i % 2 ==1]


list03 = [i for i in list01 if i % 2 == 0]
list04 = [i for i in list01 if i >3]
print(list01)
print(list02)
print(list03)
print(list04)














# list01 = []
# for item in range(1,11):
#     list01.append(item)
# print(list01)
# #列表推导式
# #list01 = [item for item in range(1,11)]
# #将list01中所有奇数存入list02
# list02 = [item for item in range(1,11) if item % 2 ==1]
# list03 = [item for item in range(1,11) if item % 2 ==0]
#
#
#
