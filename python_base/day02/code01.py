"""
在控制台录入学生信息（姓名，性别，年龄，成绩）
在一行输出串
格式：

"""

str_name = input("请输入姓名：")
str_age = input("请输入年龄：")
in_age = int(str_age)
str_sex = input("请输入性别：")
str_score = input("请输入成绩：")
float_score=float(str_score)
#int不能与字符串（str）拼接 float也不可与字符串拼接
#print("我的姓名是：" + str_name, "年龄是" + in_age,"请输入性别"+str_sex,"请输入成绩"+float_score)
#在固定格式的字符串中，插入不同
print("我的姓名是：" + str_name,"年龄是:" +str(in_age),"请输入性别:"+str_sex,"请输入成绩:"+str(float_score))