"""
随机加法考试
随机产生两个数字
在控制台中获取两个数字的相加结果
如果输入正确成绩累加10分
如果输入错误成绩扣除5分
总共5道题
总分
"""
import random
results = 0
for i in range(5):
    random_number01 = random.randint(1,10)
    random_number02 = random.randint(1,10)
    sum = int(input("请计算"+str(random_number01)+"+"+str(random_number02)+"的和"))

    if sum == random_number01 + random_number02:
        results += 10
        print("加十分")
    else:
        results -=5
        print("扣五分")
    print("总分为：",str(results))











#
# results = 0
# import random
# for i in range(5):
#     random_number01 = random.randint(1,10)
#     random_number02 = random.randint(1,10)
#     int_sum = int(input("请计算："+str(random_number01)+"+"+str(random_number02)+"=?"))
#     random_sum = random_number01 + random_number02
#     if int_sum  == random_sum:
#         results += 10
#         print("加10分")
#     else:
#         results -= 5
#         print("扣5分")
# print(results)
#
