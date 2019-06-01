"""
猜数字1.0
规则：系统产生1--100之间的随机数，
    让用户重复猜测，直到才对为止
    提示：大了 小了 猜对了
猜数字2.0
    最多只能猜10次,

 import random
 random_number = random.randint(1,100)
"""
# 1.0版本
# import random
# random_number = random.randint(1,100)
# while True:
#     int_number = int(input("猜猜是多少"))
#     if int_number > random_number:
#         print("大了")
#     elif int_number < random_number:
#         print("小了")
#     else:
#         print("猜对了")
#         break
#2.0版本  猜数字2.0
    #最多只能猜10次,
import random
random_number = random.randint(1,100)
cound = 0
while  cound < 10:
    int_number = int(input("猜猜是多少"))
    cound +=1
    if int_number > random_number:
        print("大了")
    elif int_number < random_number:
        print("小了")
    else:
        print("猜对了")
        break
else:
    print("没机会了")















# import random
# random_number = random.randint(1,100)
# while True:
#     int_number = int(input("猜一个整数："))
#     if int_number > random_number:
#         print("大了")
#     elif int_number < random_number:
#         print("小了")
#     else:
#         print("猜对了")
#         break

#2.0版本
# import random
# random_number = random.randint(1,100)
# count = 0
# while count<10:
#     count +=1
#     int_number = int(input("第"+str(count)+"次猜："))
#     if int_number > random_number:
#         print("大了")
#     elif int_number < random_number:
#         print("小了")
#     else:
#         print("猜对了")
#         break
# else:
#     #只有从 while 条件结束才执行 else
#     #从循环体内部break ，不会执行
#     print("没机会了")
