"""
在控制台中显示直角三角形的图形
for r in range(4):
    for c in range(r+1):
        print("#",end="")
    print()

"""
def print_triangle(line,char):
    """
     打印三角形
    :param（形式参数） line: 三角形高度
    :param          char:  三角形的字符
    :return:
    """
    for r in range(line):
        for c in range(r + 1):
            print(char, end="")
        print()
print_triangle(10,"1")