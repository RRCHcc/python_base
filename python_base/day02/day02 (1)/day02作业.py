"""
    温度换算器(华氏度,摄氏度,开氏度)
    摄氏度 = (华氏度 - 32) / 1.8
    华氏度 = 摄氏度*1.8 + 32
    开氏度 = 摄氏度 + 273.15
    -- 在控制台中获取华氏度,计算摄氏度
    -- 在控制台中获取摄氏度,计算华氏度
    -- 在控制台中获取摄氏度,计算开氏度
"""

float_f = float(input("请输入华氏度："))
c = (float_f-32)/1.8
print(c)

float_c = float(input("请输入摄氏度："))
f = float_c*1.8+32
print(f)

float_c = float(input("请输入摄氏度："))
k = float_c +273.15
print (k)
