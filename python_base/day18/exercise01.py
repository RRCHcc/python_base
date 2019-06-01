"""
为两个已有功能（进入后台，删除订单）增加新功能（验证权限）

"""
def validation(func):

    def wrapper(*args,**kwargs):
        print("验证权限")
        return func(*args,**kwargs)
    return wrapper
@validation
def enter_background(loginId,pwd):
    print(loginId,pwd)
    print("进入后台系统....")

@validation
def delete_order(order_id):
    print("删除%d订单"%order_id)


# enter_background("oop",123)
# delete_order(3221)


