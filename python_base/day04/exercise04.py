"""
在控制台中输入一个整数根据整数打印一个矩形
如果输入：  4

        * * * *
        *     *
        *     *
        * * * *
"""

number = int(input("请输入一个整数："))
#头
print(number*"* ")  #
for i in range(number-2):
    print("*"+" "*(number*2-3)+"*")#    " "*(number-2)
#尾
print(number*"* ")
