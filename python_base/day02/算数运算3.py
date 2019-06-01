"""
古代的称一斤是16两
在控制台中输入两，换算出是几斤几两

"""
int_liang = int(input("请输入多少两："))
jin = int_liang//16
liang = int_liang%16
print (str(jin)+"斤",str(liang)+"两")









#
# str_liang = int(input("请输入总两数："))
# jin = str_liang//16
# liang = str_liang%16
# print (str(jin)+"斤零"+str(liang)+"两")
