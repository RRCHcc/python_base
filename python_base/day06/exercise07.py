"""
练习：在控制台中显示矩形


for r in range(3):
    for c in range(5):
        print("*", end="") # 在一行输出
    print()# 换行

"""
def rectangle(line,column,char):
    """

    :param line: 矩形的高度(行
    :param column: 矩形的宽度(列
    :param char: 矩形的字符
    :return:
    """
    for r in range(line):
        for c in range(column):
            print(char,end="")
        print()

rectangle(3,5,"#")