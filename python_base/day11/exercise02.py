"""
    有若干个图形（圆形，矩形.....）
    每种图形，都可以计算面积与周长

    定义图形管理器，记录所有图形，提供据算总面积的方法
    要求增加新的图形不改变图形管理器代码
"""
class GraphicsManager:
    """
    图形面积计算器
    """

    def __init__(self):
        self.__graphics = []


    def get_graphics(self, g):
        if not isinstance(g, Graphic):
            return
        else:
            self.__graphics.append(g)

    def all_area(self,):
        all_area = 0
        for value in self.__graphics:
            all_area += value.area()
        return all_area



class Graphic:

    def area(self):
        raise NotImplementedError()

class Circular(Graphic):
    def __init__(self, r):
        self.r = r
    def area(self):
        area= 3.14*self.r**2
        return area
class Rectangular(Graphic):
    def __init__(self, long, wide, higt):
        self.long = long
        self.wide = wide
        self.higt = higt
    def area(self):
        area = self.long*self.wide*self.higt
        return area
class Triangle(Graphic):
    def __init__(self,bottom,high):
        self.bottom = bottom
        self.high = high
    def area(self):
        area = self.bottom*self.high/2
        return area


m01 = GraphicsManager()

m01.get_graphics("2,3")

m01.get_graphics(Circular(10))
m01.get_graphics(Triangle(10, 5))
m01.get_graphics(Rectangular(10, 9, 10))


print(m01.all_area())