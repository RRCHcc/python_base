"""
4,在控制台中录入5个学生信息（姓名/年龄/性别）
数据结构：列表嵌套字典
    [  {"name": xx,
        "age" : xx,
        "sex" : xx
       },
    ]
"""
list01 = []

for item in range(2):
    dict_student = {}
    dict_student["name"] = input("请输入第%d个学生姓名：" % (item+1))
    dict_student["age"] = int(input("请输入第%d个学生年龄：" % (item+1)))
    dict_student["sex"] = input("请输入第%d个学生性别" % (item+1))
    #想学生列表追加信息
    list01.append(dict_student)
    #获取所学生信息
for dict_stu in list01:
    for key, value in dict_stu.items():
        print("%s --%s"%(key,value))


