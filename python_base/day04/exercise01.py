"""
练习1：
在控制台中获取一个字符串
打印每个字符的编码值
练习2：
在控制台中循环输入编码值，显示字符，直到输入负数退出

"""
name = input("请输入字符串")
for i in name:
    print(ord(i))


# while True:
#     int_number = int(input("请输入一个编码值："))
#     if int_number < 0:
#         break
#     print(chr(int_number))



