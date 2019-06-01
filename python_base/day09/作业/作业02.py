"""
3. 创建技能类(技能名称，冷却时间，持续时间，攻击距离......)
    要求：使用属性封装变量
   创建技能列表(技能对象的列表)
   -- 查找名称是"降龙十八掌"的技能对象
   -- 查找名称是持续时间大于１０秒的的所有技能对象
   -- 查找攻击距离最远的技能对象
   -- 按照持续时间，对列表升序排列．
"""
class Skills:
    def __init__(self,
                 name="",
                 cool_time=0,
                 dura_time=0,
                 atk_rang=0
                 ):
        self.name = name
        self.cool_time = cool_time
        self.dura_time = dura_time
        self.atk_rang = atk_rang
    def print_skills(self):
        print(self.name, self.cool_time, self.dura_time, self.atk_rang)
    @property
    def name(self):

        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    @property
    def cool_time(self):
        return self.__cool_time
    @cool_time.setter
    def cool_time(self, value):
        self.__cool_time = value
    @property
    def dura_time(self):
        return self.__dura_time
    @dura_time.setter
    def dura_time(self,value):
        self.__dura_time = value
    @property
    def atk_rang(self):
        return self.__atk_rang
    @atk_rang.setter
    def atk_rang(self, value):
        self.__atk_rang = value
    @staticmethod
    def find_skills(name, list01):
        for item in list01:
            if item.name == name:
                return item
    @staticmethod
    def dura_time_find_skills(time,list01):
        dura_time_list= []
        for item in list01:
            if item.dura_time > time:
                dura_time_list.append(item)
        return dura_time_list
    @staticmethod
    def atk_rang_far(list01):
        max_rang_far = list01[0]
        for item in range(1, len(list01)):
            if list01[item].atk_rang > max_rang_far.atk_rang:
                max_rang_far = list01[item]
        return max_rang_far
    @staticmethod
    def get_dura_time_sort(list01):
        for item in range(len(list01)-1):
            for i in range(item+1,len(list01)):
                if list01[item].dura_time > list01[i].dura_time:
                    list01[item], list01[i] = list01[i], list01[item]
        return list01


"""
技能名称，冷却时间，持续时间，攻击距离
创建技能列表(技能对象的列表)
   -- 查找名称是"降龙十八掌"的技能对象
   -- 查找名称是持续时间大于１０秒的的所有技能对象
   -- 查找攻击距离最远的技能对象
   -- 按照持续时间，对列表升序排列．
"""

sk01 = Skills("降龙十八掌", 10, 12, 50)
sk02 = Skills("如来神掌", 11, 4, 45)
sk03 = Skills("佛山无影腿", 5, 30, 15)
sk04 = Skills("乾坤大挪移", 13, 13, 55)
list01 = [sk01, sk02, sk03, sk04]

# re=Skills.find_skills("降龙十八掌", list01)
# re.print_skills()

# re01 = Skills.dura_time_find_skills(10,list01)
# for i in re01:
#     i.print_skills()
# re02 =Skills.atk_rang_far(list01)
re03 = Skills.atk_rang_far(list01)
re03.print_skills()
Skills.get_dura_time_sort(list01)
for r in list01:
    r.print_skills()




