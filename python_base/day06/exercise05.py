"""
list01 = [1, 4, 7, 4, 8, 0, 6]
排序
核心： 两两元素进行比较
      发现更大的  （降序）或者更小的（升序）则交换
"""
list01 = [1, 4, 7, 4, 8, 0, 6]
for r in range(len(list01)-1):
    for c in range(r+1, len(list01)):
        if list01[r] > list01[c]:# 小的往前走 升序
            list01[r], list01[c] = list01[c], list01[r]

print(list01)



