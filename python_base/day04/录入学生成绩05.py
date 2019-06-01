"""
练习：在控制台中录入学生成绩 计算：总分，最高分，最低分
    "请输入学生总数"
    "请输入第一个学生成绩“

"""
str_amount = int(input("请输入学生总数："))
results = []
for i in range(1,str_amount+1):
    str_results =int(input("请输入第%d个学生成绩"%(i)))
    results.append(str_results)
print(results)


#
# str_amount = int(input("请输入学生总数："))
# results = []
# for i in range(1,str_amount+1):
#     str_results =int(input("请输入第%d个学生成绩:"%(i)))
#     results.append(str_results)
#
# print(results)
#
# print("总分：%d"%sum(results))
# print("最高分：%d"%max(results))
# print("最低分：%d"%min(results))
