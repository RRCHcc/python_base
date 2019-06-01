"""
        形参传递方位
            默认形参

            位置形参
                --星号元组形参：位置实参数量无限
            命名关键字形参：要求必须用关键字
                --双星号字典形参：关键字实参数量无限

        学习目标： 会调用其他人写的函数

"""

#位置形参
def fun01(a,b,c):
    pass

#星号元组形参
def fun01(*args):
    #星号元组形参，对于内部而言，就是元组
    #对于调用者而言，就是可以传递数量无限的位置实参
    print(args)

fun01()
fun01(1)
fun01(1,2,3,4)
#命名关键字形参： 强制实参使用关键字传递
#a,b 是命民关键字形参
def fun03(*,a,b):
    print(a)
    print(b)
#b 是命名关键字形参
def fun04(*a,b):
    print(a)
    print(b)

fun04(3,b=100)

# 双星号字典形参
def fun05(**kwargs):
    #对于内部而言就是字典
    #对于调用者而言就是数量无限的关键字实参
    print(kwargs)
fun05(a = "sadf",b =2,)

#调用
def fun06(*args,**kwargs):
    print(args)
    print(kwargs)
fun06(1,2,3,4,5,1, a=2)

def fun07(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

fun07(1,2,3,4,5,6,7,c=12,d= 13,e= 14,f=15)
print(1,2,3,4,sep="#@")









