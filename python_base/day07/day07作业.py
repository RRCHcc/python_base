"""
1. 自定义列表的排序函数
　　温馨提示：返回值需要吗？
"""
def get_min_number(list01):
    """
    :param list01: 列表
    :return:
    """
    #传入可变类型
    #修改的是传入对象
    for item in range(len(list01)-1):
        for i in range(item+1,len(list01)):
            if list01[item] > list01[i]:
                list01[item],list01[i] = list01[i],list01[item]

list01= [1,3,4,7,9,10,3,5,2,11,3]
print(get_min_number(list01))
print(list01)

