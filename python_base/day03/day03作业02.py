"""
在控制台中录入一个整数，判断是否为素数
（素数是只能被 1 和 自身 整除的数字）
例如：判断9能否被2--8 之间整除
     如果能，说明不是素数
     如果都不能，是素数
     提示： 循环处 2 到 该数字-1之间的整数
     在判断能否被整除
     数字 % 之间的整数 == 0：
"""
int_number = int(input("请输入一个整数")) # 假设输入是“9”
if int_number < 2:
    print("不是素数")
else:
    for number in range(2,int_number):
        if int_number % number == 0:  # if int_number%number != 0:
            print("不是素数")          # if number == int_number-1:
                                  #     print("是素数")
            break                     #有结论了，就不需要在和后面的数字比较
    else:
        print("是")

