"""
练习1
["张三丰",“无忌”,"赵敏"]
把上列改成{“张三丰”：3,“无忌”：2,,“赵敏”：2}
练习2
["张三丰",“无忌”,"赵敏"]
[101,102,103]
1）根据两个列表形成字典，键是名字，值是房间号
2）将字典的键与值进行翻转，即 k =房间号
"""
list01 = ["张三丰","无忌","赵敏"]
dict01 = {}
for i in list01:
    dict01[i] = len(i)
print(dict01)

list01 = ["张三丰","无忌","赵敏"]
list02 = [101,102,103]
dict02 = {}

dict02 = {list01[i]:list02[i] for i in range(len(list01))}

print(dict02)





# inp_str = ["张三丰","无忌","赵敏"]
# dict01 ={}
# for item  in inp_str:# item 就是每个元素
#     dict01[item] = len(item)
# print(dict01)
#
# dict01 = {item:len(item) for item in inp_str}
list01 = ["张三丰","无忌","赵敏"]
list02 = [101,102,103]
dict01 = {}
dict02 ={list01[k]:list02[k] for k in range(len(list01))}
print(dict02)

# dict03 = {value:key for key,value in dict02.items()}
# print(dict03)

list03 = [(value,key) for key,value in dict02.items()]