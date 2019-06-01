"""
list01 = [34,5,6,78,9,0,5,8,88,4]
假设一个元素就是最大值  #list01 [0]
依次与后面(从第二个开始）的余数进行比较
发现更大的，则替换假设的
最后假设就是真的最大值
"""
list01 = [34, 5, 6, 78, 9, 0, 5, 8, 88, 4]
min = list01[0]
for minnumber01 in range(1,len(list01)):
##for minnumber01 in list01[1:]: 切片会产生新的
    if min > list01[minnumber01]:
        min = list01[minnumber01]


print(min)


