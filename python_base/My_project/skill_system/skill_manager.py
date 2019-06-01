# from skill_deployer import *  只能从当前模块运行
#如果从主模块运行，不能导入会错误
from skill_system.skill_deployer import *
def manager():
    print("执行manager啦")
    skill()
