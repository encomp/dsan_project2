import unittest
from project2.collections.Node import Node
from project2.collections.DoubleLinkedList import DoubleLinkedList


class DoubleLinkedListTestCase(unittest.TestCase):

    def setUp(self):
        self.__items = [1, 2, 3, 4]
        self.__dll = DoubleLinkedList()

    def test_insert_node(self):
        for item in self.__items:
            node = Node(item)
            self.__dll.insert_node(node)
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 4)
        self.assertEqual(elements, self.__items)

    def test_insert_node_at_front(self):
        for item in self.__items:
            node = Node(item)
            self.__dll.insert_node_at_front(node)
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 4)
        self.assertEqual(elements, [4,3,2,1])

    def test_insert(self):
        for item in self.__items:
            self.__dll.insert(item)
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 4)
        self.assertEqual(elements, self.__items)

    def test_insert_at_front(self):
        for item in self.__items:
            self.__dll.insert_at_front(item)
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 4)
        self.assertEqual(elements, [4, 3, 2, 1])

    def test_remove_middle_node(self):
        nodes = list()
        for item in self.__items:
            node = Node(item)
            self.__dll.insert_node(node)
            nodes.append(node)
        self.__dll.remove_node(nodes[1])
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 3)
        self.assertEqual(elements, [1,3,4])

    def test_remove_head_node(self):
        nodes = list()
        for item in self.__items:
            node = Node(item)
            self.__dll.insert_node(node)
            nodes.append(node)
        self.__dll.remove_node(nodes[0])
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 3)
        self.assertEqual(elements, [2,3,4])

    def test_remove_tail_node(self):
        nodes = list()
        for item in self.__items:
            node = Node(item)
            self.__dll.insert_node(node)
            nodes.append(node)
        self.__dll.remove_node(nodes[3])
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 3)
        self.assertEqual(elements, [1,2,3])

    def test_remove_multiple_nodes(self):
        nodes = list()
        for item in self.__items:
            node = Node(item)
            self.__dll.insert_node(node)
            nodes.append(node)
        self.__dll.remove_node(nodes[1])
        self.__dll.remove_node(nodes[0])
        self.__dll.remove_node(nodes[3])
        self.__dll.remove_node(nodes[2])
        self.assertEqual(self.__dll.size(), 0)

        self.__dll.insert(5)
        self.__dll.insert_at_front(4)
        self.__dll.insert_at_front(3)
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 3)
        self.assertEqual(elements, [3,4,5])

    def test_remove_multiple_values(self):
        for item in self.__items:
            self.__dll.insert(item)

        self.__dll.remove(4)
        self.__dll.remove(1)
        self.__dll.remove(2)
        self.__dll.remove(3)
        self.assertEqual(self.__dll.size(), 0)

        self.__dll.insert_node(Node(9))
        self.__dll.insert_node_at_front(Node(8))
        self.__dll.insert_at_front(7)
        elements = list()
        for item in self.__dll:
            elements.append(item)

        self.assertEqual(self.__dll.size(), 3)
        self.assertEqual(elements, [7,8,9])
        print(self.__dll)

if __name__ == '__main__':
    unittest.main()
