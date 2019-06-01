"""
　猜拳
  规则：系统随机出拳，在控制台中循环猜测．
  提示：(1)将胜利的策略存入容器
              (
                  ("石头","剪刀"),
                  ("剪刀","布"),
                  ("布","石头")
              )
       (2) 将用户猜的拳与系统出拳形成一个元组
       实现三局两胜
"""
import random
#胜利策略
wins = (
    ("石头","剪刀"),
    ("剪刀","布"),
    ("布","石头")
)
#将用户猜的拳与系统出拳形成一个元组
user_win_count = 0
sys_win_count =0
while True:
    user_input_index = int(input("请输入整数（0表示石头，1表示剪刀，2表示布"))
    items = ("石头","剪刀","布")
    user_input_items = items[user_input_index]

    sys_input_index = random.randint(0,2)
    sys_input_items = items[sys_input_index]
    print(sys_input_items)
    if user_input_index == sys_input_items:
        print("平局")
    elif user_input_index in wins:
        print("赢了")
        user_win_count += 1
    else:
        print("输了")
        sys_win_count += 1

