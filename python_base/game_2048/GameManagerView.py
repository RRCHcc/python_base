"""

"""
from game_2048.GameCoreController import*

class GameManagerView:
    def __init__(self):
        self.manager = GameCoreController()

    def star_game(self):
        self.manager.put_number()
        self.manager.put_number()
        self.manager.print_map()
        self.__display_menu()

    def __display_menu(self):
        """
        显示菜单
        :return:
        """

        print("w)向上移动")
        print("s)向下移动")
        print("a)向左移动")
        print("d)向右移动")

    def __select_menu(self):

        number = input("请输入选项：")

        if number == "w":

            self.manager.move(Direction.up)

        elif number == "s":

            self.manager.move(Direction.down)

        elif number == "a":
            self.manager.move(Direction.left)

        elif number == "d":
            self.manager.move(Direction.right)



    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__select_menu()
            if self.manager.is_change:
                self.manager.put_number()
                self.manager.print_map()

