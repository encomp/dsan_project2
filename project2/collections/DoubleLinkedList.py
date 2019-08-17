from project2.collections.Node import Node


class DoubleLinkedList:

    def __init__(self):
        self.__size = 0
        self.__head = None
        self.__tail = None

    def size(self):
        return self.__size

    # Inserts a node at the front of the double linked list
    def insert_node_at_front(self, node):
        if node is None:
            return False
        if self.size() == 0:
            self.__head = node
            self.__tail = self.__head
        else:
            node.set_next(self.__head)
            self.__head.set_previous(node)
            self.__head = node
        self.__size += 1
        return True

    # Inserts an element at the front of the double linked list
    def insert_at_front(self, value):
        if value is None:
            return False
        node = Node(value)
        return self.insert_node_at_front(node)

    # Inserts a node at the end of the double linked list
    def insert_node(self, node):
        if node is None:
            return False
        if self.size() == 0:
            self.__head = node
            self.__tail = self.__head
        else:
            node.set_previous(self.__tail)
            self.__tail.set_next(node)
            self.__tail = node
        self.__size += 1
        return True

    # Inserts an element at the end of the double linked list
    def insert(self, value):
        if value is None:
            return
        node = Node(value)
        return self.insert_node(node)

    # Removes the specified node from the double linked list
    def remove_node(self, node):
        if self.size() == 0 or node is None:
            return False
        if self.size() == 1 and self.__head == node:
            self.__head = None
            self.__tail = None
            self.__size -= 1
            return True
        # Case Node to delete is head
        if self.__head == node:
            node.get_next().set_previous(None)
            self.__head = node.get_next()
            self.__size -= 1
            return True
        # Case Node to delete is tail
        if self.__tail == node:
            node.get_previous().set_next(None)
            self.__tail = node.get_previous()
            self.__size -= 1
            return True
        # Case Node to delete is in the middle
        if node.get_next() is None and node.get_previous() is None:
            return False
        next_node = node.get_next()
        previous_node = node.get_previous()
        previous_node.set_next(next_node)
        next_node.set_previous(previous_node)
        self.__size -= 1
        return True

    # Removes the specified node from the double linked list
    def remove(self, value):
        if self.size() > 0:
            node = self.__find_node(value)
            if node is not None:
                return self.remove_node(node)
        return False

    # Removes the last node from the double linked list
    def remove_last_element(self):
        if self.size() > 0:
            tmp = self.__tail
            if self.remove_node(tmp):
                return tmp
        return None

    # Finds a specific value on the double linked list
    def __find_node(self, value):
        current = self.__head
        while current:
            if current.get_value() == value:
                return current
            current = current.get_next()
        return None

    def find_value(self, value):
        node = self.__find_node(value)
        if node is not None:
            return node.get_value()
        return None

    def __iter__(self):
        current = self.__head
        while current:
            yield current.get_value()
            current = current.get_next()

    def __repr__(self):
        return "DoubleLinkedList: [{}]".format(", ".join(str(x) for x in self))
