"""
    一张纸厚度是0.01毫米（1米 = 1000毫米
问：对折多少次，可以超过珠穆朗玛峰8844.43米
"""

# while 条件
#     纸张对折
paper = 0.01/1000
count = 0
while paper > 8844.43:
    paper *= 2
    count += 1
print(count)









paper =0.01/1000
count = 0
while paper < 8844.43:
    paper *=2
    count +=1
    if paper >= 8844.43:
        print(count)











#
# paper = 0.00001# 0.01/1000
# zhu = 8844.43
# count = 0  #计算器
# while paper < zhu:
#     paper *=2
#     count +=1
#     if paper >= zhu :
#         print(count)