"""

"""
import random
import copy
import os

class GameCoreController:

    def __init__(self):
        self.__map = [
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4,
        ]
        self.__list_merge = []



    @property
    def map(self):
        return self.__map


    def zero_to_end(self):
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)


    def merge(self):
        self.zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                self.__list_merge[i + 1] = 0
        self.zero_to_end()


    def __move_left(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r]
            self.merge()
            self.__map[r][:] = self.__list_merge

    def __move_right(self):
        for r in range(len(self.__map)):
            self.__list_merge[:] = self.__map[r][::-1]
            self.merge()
            self.__map[r][::-1] = self.__list_merge

    def __move_up(self):
        for c in range(4):
            # 清空合并列表，目的：避免之前列表中的结果，对本次有影响．
            self.__list_merge.clear()
            for r in range(4):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(4):
                self.__map[r][c] = self.__list_merge[r]

    def __move_down(self):
        for c in range(4):
            self.__list_merge.clear()
            for r in range(3, -1, -1):
                self.__list_merge.append(self.__map[r][c])
            self.merge()
            for r in range(3, -1, -1):
                self.__map[r][c] = self.__list_merge[3 - r]

    def move(self,dir):
        original_map = copy.deepcopy(self.__map)
        if dir == Direction.up:
            self.__move_up()
        elif dir == Direction.down:
            self.__move_down()
        elif dir == Direction.left:
            self.__move_left()
        elif dir == Direction.right:
            self.__move_right()
        self.is_change = original_map != self.__map

    # def equal(self,original):
    #     for r in range(4):
    #         for c in range(4):
    #             if original[r][c] != self.__map[r][c]:
    #                 return  True
    #     return False

    def print_map(self):
        #清空后台
        os.system("clear")
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                print(self.__map[r][c], end="\t")
            print()


    def find_zero(self):
        list_zero = []
        for r in range(len(self.__map)):
            for c in range(len(self.__map)):
                if self.__map[r][c] == 0:
                    loc = (r,c)
                    list_zero.append(loc)
        return list_zero

    def put_number(self):
        list01 =self.find_zero()
        if len(list01) == 0:
            return
        result = random.choice(list01)
        a01 = result[0]
        a02 = result[1]
        self.__map[a01][a02]=4 if random.randint(1,10) == 1 else 2


class Direction:
    """

    """
    up = 0
    down = 1
    right = 2
    left =3

#
# if __name__ == "__main__":
#     g01 = GameCoreController()
#     g01.print_map()
#     g01.put_number()
#     g01.print_map()
#     g01.put_number()
#     g01.print_map()
#     g01.put_number()
#     g01.print_map()












