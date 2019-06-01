"""
    修改exercise03中的练习,
    如果金额不足,提示还差多少钱,如果金额够,提示应找回多少钱.
    -- 尝试:如果总价到达100元,打八折.
      在控制台中获取一个商品单价  10
      在获取一个商品数量    3
      在获取一个金额  50
计算：应该找回多少钱  20

"""

float_unit_price =float(input("请输入一个单价："))
int_amout = int(input("请输入数量："))
float_money = float(input("获取金额："))
#总金额
all_money = float_unit_price*int_amout
#满足条件打折
if  all_money >= 100:
    all_money *= 0.8
#如果钱够
if float_money > all_money:
    result = float_money - all_money
    print("找回", str(result))
else:
    result = float_money - all_money
    print("提示还差:", str(result))


#调试：让程序在指定的行中断，然后逐语句执行，我们审查程序运行过程，以及变量的取值
#1,在可能出错的中,加入断点
#2,开始调试 alt+shift+F9
#3,命中断点后（断点行是蓝色的）,然后逐语句执行F7
#…… （判断执行过程，以及变量取值）……
#4,停止调试ctrl + F2






