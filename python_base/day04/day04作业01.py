"""
    在控制台中循环录入字符串， 输入Q退出
    然后显示一个新的字符串
"""

list_result = []
while True:
    str_input = input("请输入：")
    if str_input == "q":
        break
    list_result.append(str_input)
str_result = "".join(list_result)# 使用join 进行拼接
print(str_result)

