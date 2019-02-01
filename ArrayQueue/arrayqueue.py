import array


class ArrayQueue(object):
    def __init__(self, capacity=10):
        self.__data = array.Array(capacity)

    def get_capacity(self):
        """
        获取队列的容量
        :return:
        """
        return self.__data.get_capacity()

    def get_size(self):
        """
        获取队列中已经存放的容量
        :return:
        """
        return self.__data.get_size()

    def enqueue(self, element):
        """
        向队列的尾部插入一个值
        :param element:
        """
        self.__data.add_last(element)

    def dequeue(self):
        """
        从队列的头部弹出一个值
        :return:
        """
        return self.__data.remove_first()

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return self.__data.is_empty()

    def get_front(self):
        """
        查看队列第一个元素的值
        :return:
        """
        return self.__data.get(0)

    def __str__(self):
        res = "ArrayQueue capacity: %d, size: %d\n" %(self.get_capacity(), self.get_size())
        res += "front["
        res += ", ".join(str(i) for i in self.__data)
        res += "]tail"
        return res

