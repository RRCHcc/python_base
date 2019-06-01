
list04=[
    [2, 0, 0, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2]
]

list_up = []
for r in range(0,len(list04)):
    list_up_01 = []
    for c in range(0,len(list04[r])):
        list_up_01.append(list04[c][r])
    list_up.append(list_up_01)
print(list_up)