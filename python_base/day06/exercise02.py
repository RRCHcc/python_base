"""
经理：[曹操,刘备,孙权]
技术员：[曹操,刘备,张飞,关羽]
计算：1）即是经理也是技术员的有谁  (交集
     2）是经理不是技术员的有谁
     3）是技术员不是经理的有谁
     4）张飞是经理么
     5）身兼一职的都有谁
     6）经理和技术员总共有多少人
        都用集合完成
"""
manager = ["曹操","刘备","孙权"]
technician = ["曹操","刘备","张飞","关羽"]
set_manager = frozenset(manager)
set_technician = frozenset(technician)
set_manager_tec = set_manager & set_technician
print(set_manager_tec)
set_manager_tec = set_manager - set_technician
print(set_manager_tec)
set_manager_tec = set_technician -set_manager
print(set_manager_tec)
print("张飞"in set_manager)
set_manager_tec = set_technician ^ set_manager
print(set_manager_tec)
set_manager_tec = set_technician | set_manager
print(len(set_manager_tec))