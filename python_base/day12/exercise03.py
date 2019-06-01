"""
练习：     实现向量类与整数做减法 乘法运算

"""
class Vector:
    """
    向量
    """
    def __init__(self,x):
        self.x = x
    def __str__(self):
        return "向量的x变量是：%s"%self.x
    def __sub__(self, other):
        return Vector(self.x - other)
    def __mul__(self, other):
        return  Vector(self.x * other)
    def __add__(self, other):
        return Vector(self.x+other)
    def __radd__(self, other):
        return Vector(self.x + other)
    def __rmul__(self, other):
        return Vector(self.x * other)
    def __isub__(self, other):
        self.x -= other
        return self
    def __imul__(self, other):
        self.x *= other
        return self
v01 = Vector(10)
v001 =Vector(2)
v02 = v01 -3
v03 = v01 * 3
print(v02)
print(v03)
"""
实现整数与向量做 减法/乘法
    向量与向量
"""
v04 = 4+ v01
print(v04)
v05 = 4* v01
print(v05)
v06 = v04 + v05
print(v06.x)
#实现向量类与整数 做累计减法/乘法

v01 -=1
print(v01)
v01 *= 2
print(v01)