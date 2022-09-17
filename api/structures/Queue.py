from api.models.Node import Node


class Queue:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    @property
    def size(self):
        return self.__size

    def enqueue(self, data):
        self.__size += 1
        new_node = Node(data=data)
        if self.__first is None:
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            new_node.previous = self.__last
            self.__last = new_node

    def iterate(self):
        current = self.__first
        while current:
            print("Data: ", current.data)
            current = current.next

    def remove(self):
        return_node = None
        if self.__first:
            return_node = self.__first
            if self.__first.next is not None:
                self.__first = self.__first.next
                self.__first.previous.next = None
                self.__first.previous = None
            else:
                self.__first = None
            self.__size -= 1

        return return_node

