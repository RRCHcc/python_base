"""
参照上述代码，自定义函数，my_enumerate
"""
def my_enumerata(target):
    index =0
    for item in target:
        yield (index,item)
        index +=1

list=[1,2,3,4,5,6]
for i in my_enumerata(list):
    print(i)
list02= [101,102,103]
list03= ["张三丰","张无忌","赵敏","周芷若"]

#参照上述代码，自定义函数，my_zip

def my_zip(target01,target02):
    if len(target01) < len(target02):
        for i in range(len(target01)):
            yield (target01[i],target02[i])
    else:
        for i in range(len(target02)):
            yield (target01[i],target02[i])

for r in my_zip(list02,list03):
    print(r)
 