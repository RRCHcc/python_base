"""
        2048核心算法
"""

#练习1:  定义函数将零元素移动到末尾
#0220 -->  2200
#0220 -->  2200

def game_zero_to_end(list01):
    #new_list = [ item for item in list01 if item != o]
    #new_list += [0]*list01.count(0)
    #list01[:] = new_list
    for i in range(len(list01)-1, -1,-1):
        if list01[i] == 0:
            del list01[i]
            list01.append(0)

# list01=[0,4,2,0]
# game_zero_to_end(list01)
# print(list01)
#练习2： 定义函数
#[2,2,2,0] ---->[4,0,0,0]
#[2,0,2,0] ---->[4,0,0,0]
#[2,2,2,2] ---->[4,2,0,0]
def game_merge(list02):
    #去零  [2,0,2,0]--->[2,2,0,0]
    game_zero_to_end(list02)
    #[2,2,0,2]--->[4,0,2,0]

    for item in range(0,len(list02)-1):
        #相邻且相同
        if list02[item] == list02[item+1]:
            list02[item] += list02[item+1]
            list02[item+1] = 0
    # [2,2,0,2]--->[4,0,2,0] ---->[4,2,0,0]
    game_zero_to_end(list02)

# list02 =[4,4,2,0]
# game_merge(list02)
# print(list02)

#练习3：将二维列表，以表格的格式显示在控制台中
list03 = [
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2],
]
def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[r])):
            print(map[r][c], end=" ")
        print()
# print_map(list03)

#练习4：定义向左移动函数
"""
[2 0 0 2]               [2 0 0 2]              
[2 2 0 0]    ------->   [2 2 0 0]
[2 0 4 4]               [2 0 4 4]   
[4 0 0 2]               [4 0 0 2] 
"""

def mover_right(map):
    for i in range(len(map)):
        # i = 列表
        #从右往左获取行
        #交给game_merge进行合并
        list_merge = map[i][::-1]
        game_merge(list_merge)
        map[i][::-1] = list_merge

def mover_left(map):
    for i in range(len(map)):
        # i = 列表
        #从左往右获取行
        #交给game_merge进行合并
        game_merge(map[i])
            #降维的思想
def mover_up(list_up):
    # for r in range(len(list_up)):
    list_up_03 = []
    for r in range(len(list_up)):
        list_up_01 = []
        for c in range(len(list_up)):
            list_up_01.append(list_up[c][r])
        game_merge(list_up_01[::-1])
        list_up_03.append(list_up_01)

    list_up_02 = []
    for i in range(len(list_up_03)):
        list_up_01 = []
        for j in range(len(list_up_03)):
            list_up_01.append(list_up_03[j][i])
        list_up_02.append(list_up_01)
    list_up[:] = list_up_02
def mover_down(list_down):
    list_down_03 = []
    for r in range(len(list_down)):
        list_down_01 = []
        for c in range(len(list_down)):
            list_down_01.append(list_down[c][r])
        list001= list_down_01[::-1]#   ####
        game_merge(list001)
        list_down_01 = list001[::-1]######
        list_down_03.append(list_down_01)
        print(list_down_01)
    list_down_02 = []
    for i in range(len(list_down_03)):
        list_down_01 = []
        for j in range(len(list_down_03)):
            list_down_01.append(list_down_03[j][i])
        list_down_02.append(list_down_01)
    list_down[:] = list_down_02

mover_down(list03)
print_map(list03)

"""
        2048游戏
    规则： 
        游戏运行在4*4的方格中，出现两个随机的数字
        产生随机数的策略：10%的概率是4，90%的概率是2
        用户移动方格（w s a d）,方格内的数字按照相应的规则进行合并
        如果地图有变化（数字移动过/数字合并过），再产生随机数
        胜利/游戏结束的判定：数字不能合并，也没有空白位置   
    架构：
        逻辑处理模块                 controller
        界面视图模块（控制台/pygame）  view
        数据模型模块  ...              M
        程序入口
    步骤：
        一）逻辑处理模块
            创建游戏核心类（GameCoreController
            （1）将核心算法粘贴进来
            （2）将所有参数，改为成员变量，
            （3）产生新数字
                   --计算所有空白位置（为0的位置）
                   --随机选择一个位置
                   --根据概率产生数字，存入列表的相应位置 
        二）界面视图模块
            创建游戏核心类对象
            调用核心类对象的生成数字方法
            while True：
                呈现界面
                获取用户输入，调用核心类对象的移动方法
                产生随机数
"""



















