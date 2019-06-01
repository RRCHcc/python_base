"""
一注彩票 7个球
  前 6 个是红球：1---33之间的数字，且不能重复
  最后 1 个是篮球：1--16之间的数字
  （1）在控制台中购买彩票
  （2）随机产生一注彩票
   (3)两注彩票兑奖
  import.random
  random.randint(1,33)
  random.randint(1,16)
"""
#前六个红球
#01
ticket = []
while len(ticket) < 6:
    number = int(input("请输入第%d个红球"%(len(ticket)+1)))
    if number < 1 or number > 33:
        print("输入错误")
    elif number in ticket:
        print("该号码存在")
    else:
        ticket.append(number)
while True:
    number = int(input("请输入篮球："))
    if 1 <= number <= 16:
        ticket.append(number)
        break
    else:
        print("输入错误")

for item in ticket:
    print(item)

# ticket = []
# while len(ticket) < 6:
#     number = int(input("请输入第%d个红球"%(len(ticket)+1)))
#
#     if number < 1 or number > 33:
#         print("不在范围内")
#     elif number  in ticket:
#         print("该号码已存在")
#     else:
#         ticket.append(number)
# #篮球：
# while True:
#     number = int(input("请输入篮球号码："))
#     if 1 <= number <= 16:
#         ticket.append(number)
#         break
#     else:
#         print("不在范围")
#     #获取每个元素
# for item in ticket: #将列表转换成字符串 在输出
#     print(item)
#
    #（2）随机产生一注彩票
#
# import random
#
# ticket01 = []
# while len(ticket01) < 6:
#     number = random.randint(1,33)# 如何产生不重复数字
#     if number not in ticket01:
#         ticket01.append(number)
#
#
# number = random.randint(1,16)
# ticket01.append(number)
# #排序
# temp = ticket01[:6]# 1）通过切片返回新列表
# temp.sort()# 2）对新列表进行排序
# ticket01[0:6] = temp# 3）将新列表返回给原列表
# print(ticket01)
