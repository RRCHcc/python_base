"""
4. 定义函数，判断字符串中存在的中文字符数量．
    中文编码范围：0x4E00   ord(字符)    0x9FA5
int_str = input("请输入：")
count = 0
for i in int_str:
    if 0x4E00 <= ord(i) <= 0x9FA5:
        count += 1
print(count)
"""
def chinese_amount(str_target):
    """
    :param str_target: 字符串
    :return:
    """
    count = 0
    for i in str_target:
        if 0x4E00 <= ord(i) <= 0x9FA5:
            count += 1
    return count

print(chinese_amount("我爱你520"))
