import unittest
from project2.collections.Node import Node


class NodeTestCase(unittest.TestCase):

    def test_new_node(self):
        node = Node("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertIsNone(node.get_key())
        self.assertIsNone(node.get_next())
        self.assertIsNone(node.get_previous())

    def test_set_key(self):
        node = Node("Hola")
        node.set_key(1)
        self.assertEqual(node.get_value(), "Hola")
        self.assertEqual(node.get_key(), 1)
        self.assertIsNone(node.get_next())
        self.assertIsNone(node.get_previous())

    def test_set_next(self):
        node = Node("Hola")
        node2 = Node("Mundo")
        node.set_next(node2)
        self.assertEqual(node.get_value(), "Hola")
        self.assertIsNone(node.get_key())
        self.assertEqual(node.get_next(), node2)
        self.assertIsNone(node.get_previous())

    def test_set_previous(self):
        node = Node("Hola")
        node2 = Node("Mundo")
        node.set_previous(node2)
        self.assertEqual(node.get_value(), "Hola")
        self.assertIsNone(node.get_key())
        self.assertIsNone(node.get_next())
        self.assertEqual(node.get_previous(), node2)

    def test_equal(self):
        node = Node("Hola")
        node2 = Node("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertEqual(node2.get_value(), "Hola")
        self.assertEqual(node, node2)
        self.assertEqual(node.__hash__(), node2.__hash__())
        self.assertIsNone(node.get_key())
        self.assertIsNone(node.get_next())
        self.assertIsNone(node.get_previous())

    def test_not_equal(self):
        node = Node("Hola")
        node2 = Node("Hola1")
        self.assertEqual(node.get_value(), "Hola")
        self.assertEqual(node2.get_value(), "Hola1")
        self.assertNotEqual(node, node2)
        self.assertNotEqual(node.__hash__(), node2.__hash__())
        self.assertIsNone(node.get_key())
        self.assertIsNone(node.get_next())
        self.assertIsNone(node.get_previous())

    def test_string(self):
        node = Node("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertEqual(node.__repr__(), "Hola")
        self.assertIsNone(node.get_key())
        self.assertIsNone(node.get_next())
        self.assertIsNone(node.get_previous())

if __name__ == '__main__':
    unittest.main()
