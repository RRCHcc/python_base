"""
while
"""


#死循环： 条件永远满足的循环


while True:
    str_usd =input("请输入美元")
    float_usd=float(str_usd)
    rmb=float_usd*6.788
    print(rmb)
    if input("按e键退出") == "e":
        break         #退出循环体