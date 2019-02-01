class LoopQueue(object):

    def __init__(self, capacity=10):
        self.__data = [None] * capacity
        self.__size = 0
        self.__front = 0
        self.__tail = 0

    def is_empty(self):
        """
        判断队列是否为空
        :return:
        """
        return self.__size == 0

    def get_capacity(self):
        """
        返回队列的容量
        :return:
        """
        return len(self.__data)

    def get_size(self):
        """
        返回队列的实际大小
        :return:
        """
        return self.__size

    def enqueue(self, element):
        """
        向队列尾部插入一个元素
        :param element:
        """
        if self.__size == self.get_capacity():
            self.resize(self.get_capacity()*2)
        self.__data[self.__tail] = element
        self.__tail = (self.__tail + 1) % len(self.__data)
        self.__size += 1

    def dequeue(self):
        """
        从队列头部删除一个元素
        :return:
        """
        if self.is_empty():
            raise IndexError
        res = self.__data[self.__front]
        self.__front = (self.__front + 1) % len(self.__data)
        self.__size -= 1
        if self.__size == self.get_capacity()//4 and self.get_capacity()//2 != 0:
            self.resize(self.get_capacity()//2)
        return res

    def get_front(self):
        """
        获取队列头部的值
        :return:
        """
        if self.is_empty():
            raise IndexError
        return self.__data[self.__front]

    def __str__(self):
        res = "LoopQueue capacity: %d, size: %d\n" %(self.get_capacity(), self.get_size())
        res += "front["
        i = 0
        while i < self.__size:
            res += str(self.__data[(i+self.__front) % len(self.__data)])
            if i != self.__size - 1:
                res += ", "
            i += 1
        res += "]tail"
        return res

    def resize(self, capacity):
        """
        动态生成队列的容量
        :param capacity:
        """
        new_data = [None] * capacity
        i = 0
        while i < self.__size:
            new_data[i] = self.__data[(i+self.__front) % len(self.__data)]
            i += 1
        self.__data = new_data
        self.__front = 0
        self.__tail = self.__size

