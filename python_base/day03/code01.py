"""
if  条件表达式
"""
sex = None
# if input("请输入性别：") == "男":
#     sex = 0
# else:
#     sex = 1
sex = 0 if input(input("请输入性别：") == "男") else 1
print(sex)
