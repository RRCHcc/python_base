"""
   在控制台中获取圆形的半径
   计算面积(3.14 * r 的平方)与周长(2 * 3.14 * r)
"""
float_r = float(input("请输入圆形半径:"))
perimeter =round(2 * 3.14 * float_r,3)
#round 四舍五入
area = 3.14 * float_r ** 2
print ("面积是",str(area))
print ("周长是",str(perimeter))