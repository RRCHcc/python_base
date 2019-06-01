"""
2.参照下列代码，定义根据月份返回天数的方法．
  要求：考虑２月，如果是闰年返回２９天，否则返回２８天．
    month = int(input("请输入月份:"))
    if month < 1 or month > 12:
        print("输入有误")
    elif month == 2:
        print("28天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:
        print("31天")
  #判断是否闰年
    str_year = int(input("请输入年份："))
    result= str_year%4 == 0 and str_year%100 != 0 or str_year%400 == 0
    print(result)

"""

def less_year(year):
    """

    :param year: 年份
    :return:
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400

def get_day(year,month):
    """
    :param year: 年份
    :param month: 月份
    :return:
    """
    if month < 1 or month > 12:
        return 0  # 向外返回的结果类型应该统一
    if month == 2:
        return 28 if less_year(year) else 29
    if month in (4,6,9,11):
        return 30
    return 31
print(get_day(2001,2))
