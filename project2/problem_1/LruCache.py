from project2.collections.DoubleLinkedList import DoubleLinkedList
from project2.collections.HashMap import HashMap
from project2.collections.Node import Node


class LruCache:

    def __init__(self, capacity=10):
        self.__capacity = capacity
        self.__dll = DoubleLinkedList()
        self.__hm = HashMap(capacity)
        return

    def capacity(self):
        return self.__capacity

    def size(self):
        return self.__hm.size()

    # Retrieve item from provided key. Return -1 if nonexistent.
    def get(self, key):
        if key is not None:
            node = self.__hm.get(key)
            # Move the node to the top on the double linked list
            if node is not None:
                self.__dll.remove_node(node)
                self.__dll.insert_node_at_front(node)
                return node.get_value()
        return -1

    # Set the value if the key is not present in the problem_1. If the problem_1 is at capacity remove the oldest item.
    def set(self, key, value):
        if key is not None:
            # if the problem_1 is at capacity remove the oldest item
            if self.size() == self.capacity():
                node = self.__dll.remove_last_element()
                self.__hm.remove(node.get_key())
            node = self.__hm.get(key)
            # Node is on the map
            if node is not None:
                node.set_value(value)
                self.__dll.remove_node(node)
            # Node is not on the map
            else:
                node = Node(value)
                node.set_key(key)
                self.__hm.put(key, node)
            self.__dll.insert_node_at_front(node)
            return True
        return False

    def __repr__(self):
        return "LRU Cache:\n\t{}\n\t{}".format(self.__hm, self.__dll)
