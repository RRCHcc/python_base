"""
在控制台输入 月，日
    计算这是一年的第几天
例如：3月5日
    累加1月，2月总天数，在累加3月的5天
    #将每个月的天数放入元组
"""
day_of_month = (31,28,31,30,31,30,31,30,31,30,31)
month = int(input("请输入月份："))
day = int(input("请输入天数："))
if month < 1 or month>12 or day > 31 or day < 1:
    print("输入错误")
elif month == 2 and day > 29:
    print("超过该月份天数")
else:
    result = sum(day_of_month[:month-1])
    result += day
    print(result)














month = int(input("请输入月份："))
day = int(input("请输入天："))
day_of_month = (31,28,31,30,31,30,31,30,31,30,31)
result = 0
if month < 1 or month > 12 or day < 1 or day >31:
    print("输入错误")
elif month == 2 and day > 29:
    print("超过该月份天数")
    # for i in range(month-1):
    #     result += day_of_month[i]
else:
    result = sum(day_of_month[:month-1])
    result += day
    print(result)





