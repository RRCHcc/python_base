"""
 一个球从100米的高度落下，每次弹回原高度的一半，
  总共弹次多少次？（假定最小弹起高度是0.01米）
  总过走了多少米？
"""
number = 0
highly = 100               #当前高度
meter = highly
# higntly / 2弹起来的高度 > 0.01
while highly / 2 > 0.01:   # 可以弹起的条件
    highly /= 2            #高度计算（高度减半
    meter += 2*highly      #弹了多少米 累加上下距离
    number += 1            #计算
print(number)
print(round(meter,2))      #round(变量,2)保留两位小数

