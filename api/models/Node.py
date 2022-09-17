
class Node:

    def __init__(self, next=None, previous=None, data=None):
        self.__next = next
        self.__previous = previous
        self.__data = data

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @next.deleter
    def next(self):
        self.__next = None

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        self.__previous = value

    @previous.deleter
    def previous(self):
        self.__previous = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @data.deleter
    def data(self):
        self.__data = None

