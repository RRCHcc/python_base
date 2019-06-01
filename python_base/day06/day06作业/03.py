"""
3.参照下列代码，定义获取最小值方法．
    min = list01[0]
    for i in range(1, len(list01)):
        # 发现更大的，则替换假设的．
        if min > list01[i]:
            min = list01[i]
    print(min)
"""
def get_min(list,):
    """

    :param list: 列表
    :return:
    """
    minnumber = list[0]
    for i in range(1, len(list)):
        # 发现更大的，则替换假设的．
        if minnumber > list[i]:
            minnumber = list[i]
    return minnumber

list = [-111, 2, -3, -54, 5, 6, 7]
print(get_min(list))