"""
        在控制台录入学生姓名
    要求： 姓名不能重复
          如果录入esc，则停止录入打印每个学生姓名

"""

list = []
cound = 1
while True:
    name = input("请输入第%d个学生："%(cound))
    if name == "esc":
        break
    if name not in list:
        list.append(name)
        cound += 1
for item in list:
    print(item)
















list = []
while True:
    name = input("请输入第%d个学生"%(len(list)+1))
    if name == "esc":
        break
    if name not in list:
        list.append(name)
for item in list:
    print(item)


















list = []
while True:
    name = input("请输入第%d学生姓名："%(len(list)+1))
    if name == "esc":
        break
    if name not in list:
        list.append(name)
for item in list:#  查列表元素
    print(item)