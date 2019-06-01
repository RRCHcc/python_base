"""
练习3
在控制台中输入一个月份
返回该月份的天数
1 3 5 7 8 10 12(31天）
4 6 9 11(30天）
2 （当28天
"""
int_month = int(input("输入一个月份"))
if int_month<1 or int_month>12:
    print("输入有误")
elif int_month == 2:
    print("该月份有28天")
elif int_month == 4 or int_month == 6 or int_month == 9 or int_month == 11:
    print("该月份有30天")
else:
    print("该月份有31天")














#
# int_month = int(input("请输入一个月份："))
# if int_month < 1 or int_month > 12:
#     print("输入有误")
# elif int_month ==2:
#     print("该月份有28天")
# elif intmonth == 4 or int_month == 6 or int_month == 9 or int_month == 11:
#     print("该月份有30天")
# else:
#     print("该月份有31天")