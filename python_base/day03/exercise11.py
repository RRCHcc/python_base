"""
    累加1--100之间 能被3整除的整数和

"""
all_sum = 0
for number in range(1,101):
    if number%3 == 0:
   # if number%3 != 0:
    #    continue
        all_sum += number
print(all_sum)


















# all_sum = 0
# for number in range(1,101):
#     if number%3 == 0:
#         all_sum += number
# print(all_sum)

all_sum = 0
for number in range(1,101):
    #如果不满足条件(题目条件） 则 跳过
    if number % 3 != 0:#(<---满足条件跳过)
        continue#跳过
    all_sum += number
print(all_sum)


