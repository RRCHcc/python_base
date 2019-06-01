"""
        工具类
"""
class ListHelper:
    """
        查找列表中满足条件的所有元素
    :param target: 列表
    :param func_condition: 条件
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
    :return:
    """
    @staticmethod
    def find_all(target, func_condition):
        for item in target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_first(target, func_condition):
        """
        根据条件查找第一个元素
        :param target:
        :param func_condition:
        :return:
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        """
        for item in target:
            if func_condition(item):
               return item
    @staticmethod
    def select(target, func_condition):
        """
            筛选列表中指定条件的数据
        :param target:
        :param func_condition:
        :return:
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        """
        for item in target:
            yield func_condition(item)

    @staticmethod
    def sum(target,func_condition):
        """
        计算列表中指定条件的所有元素和
        :param target:
        :param func_condition:
        :return:
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        """
        result = 0
        for item in target:
            result += func_condition(item)
        return result
    @staticmethod
    def find_last_demo(target,func_condition):
        """
        获取满足条件的最后一个对象
        :param target: 列表
        :param func_condition: 条件
        :return:
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        """

        for item in range(len(target)-1,-1,-1):
            if func_condition(target[item]):
                 return target[item]
    @staticmethod
    def judge(target,func_condition):
        """
        判断列表中是否包含某个元素
        :param target:
        :param func_condition:
        :return:
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值

        """
        for item in target:
            if func_condition(item):
                return True
        return False
    @staticmethod
    def total(target, func_condition):
        """
        获取满足条件对象总数
        :param target:
        :param func_condition:
        :return:
            函数／方法类型
            －－　参数：列表中的元素
            －－　返回值：是否满足条件bool值
        """
        count = 0
        for item in target:
            if func_condition(item):
                count += 1
        return count
    @staticmethod
    def delete(target, func_condition):
        """
        删除满足条件的所有对象
        :param target: 列表
        :param func_condition: 条件
        :return:
        """
        del_count=0#删除元素数量
        for item in range(len(target) - 1, -1, -1):
            if func_condition(target[item]):
                del target[item]
                del_count += 1
        return del_count
    @staticmethod
    def find_max(target,func_condition):
        """
        获取满足条件的最大值
        :param target:
        :param func_condition_max:
        :param func_condition:
        :return:
        """
        max_number = target[0]
        for item in range(1, len(target)):
            if func_condition(max_number) < func_condition(target[item]):
                max_number = target[item]
        return max_number
    @staticmethod
    def order_by(target,func_condition):
        """
        根据条件进行升序排列
        :param target:
        :param func_condition:
        :return:
        """
        for i in range(len(target) - 1):
            for item in range(i, len(target)):
                if func_condition(target[i]) > func_condition(target[item]):
                    target[i], target[item] = target[item], target[i]
    @staticmethod
    def find_min(target, func_condition):
        """
        根据条件获取最小值
        :param target:
        :param func_condition:
        :return:
        """
        min = target[0]
        for item in range(1, len(target)):
            if func_condition(min) > func_condition(target[item]):
                min = target[item]
        return min
    @staticmethod
    def order_by_descending(target,func_condition):
        """
        根据条件进行降序排列
        :param target:
        :param func_condition:
        :return:没有返回值，直接对原列表操作
        """
        for i in range(len(target) - 1):
            for r in range(i + 1, len(target)):
                if func_condition(target[i]) < func_condition(target[r]):
                    target[i], target[r] = target[r], target[i]
    @staticmethod
    def lntelligent_sorting(target,func_condition):
        """
        根据条件 升/降 排序
        :param target:
        :param func_condition:排序逻辑
                              类型是函数
                              参数是列表中两个元素
                              返回值是比较结果
                              方法是比较条件
        :return:
        """
        for i in range(len(target) - 1):
            for r in range(i + 1, len(target)):
                if func_condition(target[i],target[r]):
                    target[i], target[r] = target[r], target[i]










