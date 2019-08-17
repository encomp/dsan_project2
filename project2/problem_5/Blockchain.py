from project2.collections.DoubleLinkedList import DoubleLinkedList
from project2.problem_5.Block import Block


class Blockchain:

    def __init__(self):
        self.__dll = DoubleLinkedList()
        self.__prior_block = None

    def add(self, data):
        if data is None:
            return False
        if self.__dll.size() == 0:
            self.__prior_block = Block(data)
        else:
            block = Block(data, self.__prior_block.get_hash())
            self.__prior_block = block
        self.__dll.insert(self.__prior_block)
        return True

    def size(self):
        return self.__dll.size()

    def __iter__(self):
        for item in self.__dll:
            yield item

    def __repr__(self):
        return "\n".join(str(x) for x in self)
