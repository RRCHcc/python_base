"""
练习：在二维列表当中获取2,3位置向左三个元素
                    0,2位置向下两个元素
                    2,0位置右上两个元素

"""
class Vector2:
    """
        向量
        二维列表工具

    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 将函数转移到类中，就是静态方法．
    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def left():
        return Vector2(0,-1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)

    @staticmethod
    def right_up():
        return Vector2(-1, 1)


class DoubleListHelper:
    """
        二维列表助手类
            定义：在开发过程中，所有对二维列表的常用操作．
    """

    @staticmethod
    def get_elements(list_target, v_pos, v_dir, count):
        result = []
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result
"""
练习：在二维列表当中获取2,3位置向左三个元素
                     0,2位置向下两个元素
                     2,0位置右上两个元素

"""

list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]
# re01 = DoubleListHelper.get_elements(
#     list01, Vector2(2, 3), Vector2.left(), 3
# )
# print(re01)
# re02 = DoubleListHelper.get_elements(
#     list01, Vector2(0, 2), Vector2.down(), 2
# )
# print(re02)
# re03 = DoubleListHelper.get_elements(
#     list01, Vector2(2, 0), Vector2.right_up(), 2
# )
# print(re03)
#










