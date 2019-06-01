"""
练习1：
在控制台中获取一个月份
打印季节
"""
int_month = int(input("请输入一个月份"))
if int_month < 1 or int_month>12:
    print("输入有误")
elif int_month <= 3:
    print("春天")
elif int_month <= 6:
    print("夏天")
elif int_month <= 10:
    print("秋天")
else:
    print("冬天")







# int_month = int(input("请输入一个月份："))
#
# if int_month<1 or int_month>12:
#     print ("输入有误")
# elif int_month<=3:
#     print("春天")
# elif int_month<=6:
#     print("夏天")
# elif int_month<=9:
#     print("秋天")
# else:
#     print("冬天")
