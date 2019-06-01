"""
1. 参照下列代码，定义判断是否是奇数的方法．
    number = int(input("请输入整数:"))
    if number % 2 == 1:
        print("奇数")
    else:
        print("偶数")
"""
def get_odd(number):
    """

    :param number: 需要判断的数
    :return:
    """
    return True if number % 2 == 1 else False


print(get_odd(-36631))