"""
练习1：
在控制台中获取一个月份
打印季节
定义： 根据月份，判断季节的方法
"""
def month_season(int_month):
    """

    :param int_month: 月份
    :return:
    """
    if int_month < 1 or int_month>12:
        return False
    if int_month <= 3:
        return "春天"
    if int_month <= 6:
        return "夏天"
    if int_month <= 10:
        return "秋天"
    return "冬天"
season = month_season(5)
print(season)