"""
为两个已有功能 添加新功能（验证账号

"""
def verify_permission(func):
    def wrapper(*args,**kwargs):
        print("验证权限")
        return func(*args, **kwargs)
    return wrapper

@verify_permission
def deposit(money):
    print("存款",money)
@verify_permission
def withdraw():
    print("取钱")
    return 10000

deposit(50000)
print(withdraw())










