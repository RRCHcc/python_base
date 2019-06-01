"""
程序入口

"""

from ui import StudentManagerView

#从当前模块运行，执行程序逻辑
if __name__ == "__main__":
    view =StudentManagerView()#创建视图类对象
    view.main()

