"""
练习：
    定义方法，在控制台中获取成绩（int/float）（1~100）
    要求：如果输入有误重新输入，知道输入正确为止

"""

def score():
    while True:
        try:
            stu_score = float(input("请输入成绩："))
        except :
            print("成绩输入错误，重新输入")
            continue
        if 1 <= stu_score <= 100:
            return  stu_score
        print("成绩不在范围内")
