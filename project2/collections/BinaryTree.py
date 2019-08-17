from project2.collections.TreeNode import TreeNode


class BinaryTree:

    def __init__(self, root=None):
        self.__root = root
        self.__size = 0

    def get_root(self):
        return self.__root

    def insert(self, value):
        if value is None:
            return False
        self.__root = self.__insert_recursive(self.__root, value)
        return True

    def __insert_recursive(self, current, value):
        if current is None:
            return TreeNode(value)

        if value < current.get_value():
            left = self.__insert_recursive(current.get_left(), value)
            current.set_left(left)
        elif value > current.get_value():
            right = self.__insert_recursive(current.get_right(), value)
            current.set_right(right)
        return current

