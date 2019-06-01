"""
练习： 选出所有成绩大于90的学生
"""

def get_score(target):
    for item in target:
        if item.score > 90:
            yield item
