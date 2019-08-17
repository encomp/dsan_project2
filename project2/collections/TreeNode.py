

class TreeNode:

    def __init__(self, value, left=None, right=None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_value(self):
        return self.__value

    def set_left(self, left):
        self.__left = left
        return

    def get_left(self):
        return self.__left

    def set_right(self, right):
        self.__right = right
        return

    def get_right(self):
        return self.__right

    def is_leaf(self):
        return self.get_left() is None and self.get_right() is None

    def __repr__(self):
        return "{}".format(self.__value)
