"""
练习3
在控制台中输入一个月份
返回该月份的天数
1 3 5 7 8 10 12(31天）
4 6 9 11(30天）
2 （当28天
使用元组
"""
month = int(input("请输入月份："))
day_of_month = (31, 28, 31,30, 31, 30, 31, 31, 30, 31, 30, 31)
if month > 12 or month < 1:
    print("输入错误")
else:
    print(day_of_month[month-1])












month =int(input("请输入月份："))
if month<1 or month>12:
    print("输入错误")
else:
    day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
    print(day_of_month[month-1])













int_month = int(input("输入一个月份"))
if int_month<1 or int_month>12:
    print("输入有误")
else:
    #将每月的天数，存入元组
    day_of_month = (31,28,31,30,31,30,31,30,31,30,31)
    print(day_of_month[int_month-1])



# #利用元组
# int_month = int(input("输入一个月份"))
# if int_month<1 or int_month>12:
#     print("输入有误")
# elif int_month == 2:
#     print("该月份有28天")
# #elif int_month == 4 or int_month == 6 or int_month == 9 or int_month == 11:
# elif int_month in (4,6,9,11):
#     print("该月份有30天")
# else:
#     print("该月份有31天")