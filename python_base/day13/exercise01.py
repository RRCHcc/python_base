"""
测试向量
以三种方式测试工具类中的方法

练习：在二维列表当中获取2,3位置向左三个元素
                    0,2位置向下两个元素
                    2,0位置右上两个元素
"""
# from day09 import double
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
import double_list as double

c01 = double.DoubleListHelper.get_elements(
    list01,double.Vector2(2,3),double.Vector2.left(),3
)
print(c01)

from double_list import DoubleListHelper as helper
from double_list import Vector2 as vet

c01 = helper.get_elements(
    list01,vet(2,3),vet.left(),3
)
print(c01)




