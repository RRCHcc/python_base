"""
        ******
        ######
        ******
        ######

"""
# for r in range(4):
#     for c in range(6):
#         if r % 2 == 0:
#             print("*", end="") # 在一行输出
#         else:
#             print("#", end="")
#     print()# 换行

"""
        #
        ##
        ###
        ####
"""
# for r in range(4):
#     for c in range(r+1):
#         print("#",end="")
#     print()
#
"""
        ####
         ###
          ##
           #
"""
for r in range(20):
    for c in range(r):
        print(" ",end="")
    for c in range(20-r):
        print("#",end="")
    print()

