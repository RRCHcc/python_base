"""
练习1:在控制台输入一个整数，判断是奇数还是偶数，要求用真值表达式
练习2:在控制台中获取一个年份，如果闰年给变量day赋值29,赋值28
"""
#练习1
# int_integer = int(input("请输入一个整数"))
# if int_integer < 1:
#     print("输入有误")
# elif int_integer%2 ==0:
#     print("偶数")
# else:
#     print("奇数")
#练习2

# year = int(input("请输入一个年份"))
# day = 29 if not year%4 and year%100 or not year%400 else 28#(条件表达式）
# #(条件表达式）变量  =  结果1 if 条件 else 结果2
# print(day)


num01 = 800
num02 = 900
num03 = num01
print(num01 is num02) # false
print(id(num01) ==  id(num02))
print(num03 is num01) #  true








#int_number = int(input("请输入一个整数"))
# int_number%2 == 1:
# if int_number%2:#bool( 5 % 2 )
#     print("奇数")
# else:
#     print("偶数")
#

#
#year = int(input("请输入一个年份："))
# day = 29 if  year%4 == 0 and year%100 != 0 or year%400 == 0 else 28
# 下列简洁
#day = 29 if not year%4 and year%100 or not year%400 else 28