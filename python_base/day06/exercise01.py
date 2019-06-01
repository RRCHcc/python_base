"""
在控制台中录入多少个字符串
按 q 退出 ， 再显示所有不重复的字符串
"""

set01 = set()
while True:
    info = input("请输入：")
    if info == "q":
        break
    else:
        set01.add(info)

for item in set01:

    print(item)