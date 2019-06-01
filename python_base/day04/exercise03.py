"""
在控制台中，获取一个字符串

#1  打印第一个字符
#2  打印最后一个字符
#3  如果是奇数，打印中间的字符
#4  打印倒数3个字符
#5  倒叙打印字符串

"""
number = input("请输入：")
print(number[0])#1 索引
print(number[-1])#2
if len(number) %2 == 1:#3
    print(number[len(number)//2])
else:
    print("没有中间数")
print(number[-3:])#4
print(number[::-1])#5


