

class Node:

    def __init__(self, value):
        self.__value = value
        self.__key = None
        self.__next = None
        self.__previous = None

    def set_value(self, value):
        self.__value = value
        return

    def get_value(self):
        return self.__value

    def set_key(self, key):
        self.__key = key
        return

    def get_key(self):
        return self.__key

    def set_next(self, next):
        self.__next = next
        return

    def get_next(self):
        return self.__next

    def set_previous(self, previous):
        self.__previous = previous
        return

    def get_previous(self):
        return self.__previous

    def __repr__(self):
        return "{}".format(self.__value)

    def __hash__(self):
        return hash(self.__value)

    def __eq__(self, other: object) -> bool:
        return self.__class__ == other.__class__ and self.__value == other.__value
