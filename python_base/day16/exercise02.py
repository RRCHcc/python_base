"""
练习：
        使用列表推导式，与生成器表达式，获取list02中大于三的数据
"""
list02 = [2, 3, 4, 6]
result = [item for item in list02 if item > 3]
print(result)

result = (item for item in list02 if item > 3)
for item in result:#循环一次，计算一次，返回一次
    print(item)
