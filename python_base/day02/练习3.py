"""
在控制台中获取一个总秒数
计算几小时零几分钟零几秒钟

提示：商指的是分钟数，余数表示剩下的秒数
# total_second // 60 商指的是分钟数,再除以60,商表示小时,余数表示剩下的分钟

"""

int_seconds = int(input("请输入总秒数："))
hour = int_seconds//3600
minutes = int_seconds//60%60
seconds = int_seconds%60

print (str(hour)+"小时",str(minutes)+"分钟",str(seconds)+"秒钟")
