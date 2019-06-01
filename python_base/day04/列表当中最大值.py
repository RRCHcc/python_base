"""
list01 = [34,5,6,78,9,0,5,8,88,4]
假设一个元素就是最大值  #list01 [0]
依次与后面(从第二个开始）的余数进行比较
发现更大的，则替换假设的
最后假设就是真的最大值
"""
# list01 = [34,5,6,78,9,0,5,8,88,4]
# maxnum = list01[0]
# for maxnumber01 in range(1,len(list01)):
#     if maxnum < list01[maxnumber01]:
#         maxnum = list01[maxnumber01]
#     print(maxnum)
#



list01 = [34,5,6,78,9,0,5,8,88,4,]
maxnum = list01[0]  #假设列表当中第一个为最大值
for maxnumber01 in range(1,len(list01)):

    if maxnum < list01[maxnumber01]:
        maxnum = list01[maxnumber01]
print(len(list01))# 列表长度
print(maxnum)

