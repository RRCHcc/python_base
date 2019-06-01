"""
1.
在控制台中输入一个整数
如果是奇数，则显示奇数否则显示偶数

"""
#1
# int_num01 = int(input("请输入一个整数："))
#
# if int_num01%2 == 0:
#     print ("偶数")
# else:
#     print("奇数")

   #  2.
   #  在控制台中输入一个年份
   #  如果是闰年则显示闰年，否则显示平年.

int_year01 = int(input("请输入一个年份："))

if int_year01%4 == 0 and int_year01%100 != 0 or int_year01%400 == 0:
    print("闰年")
else:
    print("平年")
