"""
练习1： 定义函数 输入年月日 返回 星期
        星期一 星期二 星期三
练习2： 定义函数，根据生日（年 月 日）返回活了多少天
        根据年月日构建时间元组
        根据构建的时间元组 获取时间戳
        使用当前减去 获取时间戳
        将活的秒数换算成天数
"""
import time


#
# def week(year,month,day):
#     get_week = time.strptime("%d/%d/%d"%(year, month, day), "%Y/%m/%d")
#     weeks={
#         0:"星期一",
#         1:"星期二",
#         2:"星期三",
#         3:"星期四",
#         4:"星期五",
#         5:"星期六",
#         6:"星期日"
#     }
#     return weeks[get_week[6]]
# print(week(2019,4,18))

def life_day(year,month,day):
    get_week = time.strptime("%d/%d/%d"%(year, month, day), "%Y/%m/%d")
     # 获取时间戳
    life_seconds = time.time() - time.mktime(get_week)
    return life_seconds/60/60//24

# print(life_day(1993,9,22))

print(time.time())

