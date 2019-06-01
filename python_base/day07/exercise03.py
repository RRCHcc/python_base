"""
定义函数：根据天/小时/分钟 ，计算总秒数：

"""
def get_second(day=0 ,hour=0, minute=0):


    return day*86400+ hour *3600+ minute *60
re = get_second(364,24,60)
print(re)