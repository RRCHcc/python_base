"""
5. 扩展练习(定义函数，返回指定范围内的素数)
例如：１－－１００　　

"""

def prime_number(start_number,end_number):
    """
        生成指定范围内的素数
    :param start_number: 开始值
    :param end_number: 结束值
    :return:范围内的素数
    """
    list01= []
    for number in range(start_number, end_number+1):
        if is_prime(number):
            list01.append(number)
    return list01


def is_prime(number):
    """
        是否为素数
    :param number: 需要判定的数字
    :return: 是不是素数
    """
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

re = prime_number(-5,100)
print(re)












