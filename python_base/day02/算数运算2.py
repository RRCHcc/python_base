"""
从控制台中获取小时/分钟/秒，计算总秒数

"""

int_hour = int(input("请输入小时："))
int_minute = int(input("请输入分钟："))
second = int(input("请输入秒数："))

hour = int_hour*3600
minute = int_minute*60

result = hour+minute+second
print (result)







#
#
# hour = input("多少小时：")
# hour = int(hour)
# minute = int(input("多少分钟："))
# second = int(input("多少秒："))
# time = hour*3600 + minute*60 +second
# print("总秒数是："+str(time))