import array


class Stack(object):
    def __init__(self, number=10):
        self.__data = array.Array(number)

    def pop(self):
        """
        从栈顶弹出一个元素
        :return:
        """
        return self.__data.remove_last()

    def push(self, element):
        """
        从栈顶压入一个元素
        :param element:
        """
        self.__data.add_last(element)

    def is_empty(self):
        """
        判断是否是空栈
        :return:
        """
        return self.__data.is_empty()

    def peek(self):
        """
        查看栈顶元素
        :return:
        """
        return self.__data.get(self.get_size()-1)

    def get_size(self):
        """
        获取栈中元素的个数
        :return:
        """
        return self.__data.get_size()

    def __str__(self):
        res = "Stack size: %d, capacity: %d\n" %(self.__data.get_capacity(), self.__data.get_size())
        res += "["
        res += ", ".join(str(i) for i in self.__data)
        res += "]"
        return res


