"""
练习二
在控制台中输入一个季度
显示季度中的月份
"""
int_quarter = int(input("请输入一个季度"))
if int_quarter < 1 or int_quarter > 4:
    print("输入有误")
elif int_quarter == 1:
    print("该季度有1.2.3")
elif int_quarter == 2:
    print("该季度有4.5.6")
elif int_quarter == 3:
    print("该季度有7.8.9")
else:
    print("该季度有10.11.12")









# int_quarter = int(input("请输入一个季度："))
# if 1 > int_quarter or int_quarter > 4:
#     print("输入有误")
# elif int_quarter == 1:
#     print ("该季度的月份有：一月，二月，三月")
# elif int_quarter == 2:
#     print ("该季度的月份有：四月，五月，六月")
# elif int_quarter == 3:
#     print ("该季度的月份有：7月，8月，9月")
# else:
#     print ("该季度有：10.11.12")