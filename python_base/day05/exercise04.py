"""
字典练习：
练习二
在控制台中输入一个季度
显示季度中的月份
"""
seasons = {1:"1,2,3,",
           2:"4,5,6,",
           3:"7,8,9,",
           4:"10,11,12"
}
season = int(input("请输入季度："))
if season not in seasons:
   print("输入错误")
else:
    value = seasons[season]
    print(value)

















seasons = {1:"一月，二月，三月",
         2:"四月，五月，六月",
         3:"、七月，八月，九月",
         4:"十月，十一月，十二月"
}#建议写多个行时 格式
season = int(input("请输入一个季度"))
#if season < 1 or season > 4:#  not in 也可以判断
if season not in seasons:# 只能判断键 是否在字典里
    print("输入有误")
else:
    value = seasons[season]
    print(value)

