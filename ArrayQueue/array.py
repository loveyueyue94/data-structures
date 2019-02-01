
class Array(object):
    def __init__(self, number=10):
        self.__size = 0
        self.__data = [None] * number
        self.current = 0

    def add(self, index, element):
        """
        向指定位置插入元素
        :param index: 要插入的位置
        :param element: 要插入的元素
        """
        if index < 0 or index > self.__size:
            raise IndexError
        if self.__size == self.get_capacity():
            self.resize(self.get_capacity() * 2)
        i = self.__size
        while i > index:
            self.__data[i] = self.__data[i - 1]
            i -= 1
        self.__data[index] = element
        self.__size += 1

    def add_last(self, element):
        """
        向尾部插入一个元素
        :param element: 要插入的元素
        """
        self.add(self.__size, element)

    def add_first(self, element):
        """
        向头部插入一个元素
        :param element: 要插入的元素
        """
        self.add(0, element)

    def remove(self, index):
        """
        删除指定索引的元素
        :param index:
        :return: 并将删除的元素返回
        """
        if index < 0 or index >= self.__size:
            raise IndexError
        res = self.__data[index]
        while index < self.__size-1:
            self.__data[index] = self.__data[index+1]
            index += 1
        self.__size -= 1
        if self.__size == self.get_capacity()//4 and self.get_capacity()//2 != 0:
            self.resize(self.get_capacity()//2)
        return res

    def remove_last(self):
        """
        删除最后一个元素
        :return:
        """
        return self.remove(self.__size-1)

    def remove_first(self):
        """
        删除第一元素
        :return:
        """
        return self.remove(0)

    def set(self, index, element):
        """
        修改元素的值
        :param index: 索引
        :param element: 新值
        """
        if index <0 or index >= self.__size:
            raise IndexError("index is error")
        self.__data = element

    def get(self, index):
        """
        获取元素的值
        :param index: 索引
        :return: 返回值
        """
        if index < 0 or index >= self.__size:
            raise IndexError("index is error")
        return self.__data[index]

    def is_empty(self):
        """
        检查数组是否为空
        :return: True空 False非空
        """
        return self.__size == 0

    def get_size(self):
        """
        返回数组的长度
        :return: 长度值
        """
        return self.__size

    def get_capacity(self):
        """
        返回数组的容量
        :return: 容量值
        """
        return len(self.__data)

    def find(self, element):
        """
        通过值返回索引
        :param element: 要查找的值
        :return: 找到返回索引，否则返回-1
        """
        for i, e in enumerate(self.__data[0: self.__size]):
            if e == element:
                return i
        return -1

    def contains(self, element):
        """
        检查数组中是否包含element
        :param element:
        :return:
        """
        return self.find(element) != -1

    def resize(self, size):
        """
        动态扩张数组的大小
        :param size: 需要扩张的大小
        """
        new_data = [None] * size
        for i, e in enumerate(self.__data[0: self.__size]):
            new_data[i] = e
        self.__data = new_data

    def __iter__(self):
        """
        使array类可迭代
        :return:
        """
        return self

    def __next__(self):
        """
        配合iter魔法方法使得该类可迭代
        :return:
        """
        if self.current < self.__size:
            res = self.__data[self.current]
            self.current += 1
            return res
        else:
            self.current = 0
            raise StopIteration

    def __str__(self):
        res = "Array size: %d, capacity: %d \n" %(self.__size, self.get_capacity())
        res += "["
        res += ", ".join(str(i) for i in self.__data[0:self.__size])
        res += "]"
        return res
