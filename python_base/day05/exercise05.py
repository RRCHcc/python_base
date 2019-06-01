"""
在控制台中录入一个字符串
打印这个字符串中的字符以及出现的次数
        abcdbcd
        a字符 1次
        b字符 2次
        c字符 2次
        d字符 2次
统计  字 出现的次数
"""
















dict01 = {}
str_name = input("请输入：")
for k in str_name:
    if k not in dict01:
        dict01[k] = 1
    else:
        dict01[k] +=1
for k,v in dict01.items():#获取字典当中所有元素
    print(k,v)














dict01 = {}
z01 = input("请输入：")
for item in z01:
    if item not in dict01:# 判断字典当中有没有某些键
        dict01[item] = 1
    else:                   #否则次数增加
        dict01[item] += 1

for k,v in dict01.items():
    print(k,v)
