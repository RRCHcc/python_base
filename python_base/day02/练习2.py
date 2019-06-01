"""
  练习2：在控制台中获取4位整数1234
        计算每位相加和
如何获取个位(求余
如何获取十位(取三位再求余
如何获取百位（同上

加等于（累加 +=）
"""

num01 = int(input("请输入一个四位整数："))
# num_qian = num01//1000
# num_bai = num01//100%10
# num_shi = num01//10
# num_ge = num01%10
result=num01//1000+num01//100%10+num01//10%10+num01%10
print ("数字和为：",str(result))