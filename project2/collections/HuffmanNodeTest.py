import unittest
from project2.collections.HuffmanNode import HuffmanNode

class HuffmanNodeTest(unittest.TestCase):

    def test_new_node(self):
        node = HuffmanNode('a', 1)
        self.assertEqual(node.get_letter(), 'a')
        self.assertEqual(node.get_frequency(), 1)
        self.assertIsNone(node.get_code())
        self.assertIsNone(node.get_left())
        self.assertIsNone(node.get_right())

    def test_set_code(self):
        node = HuffmanNode('a', 1)
        self.assertEqual(node.get_letter(), 'a')
        self.assertEqual(node.get_frequency(), 1)
        self.assertIsNone(node.get_code())
        self.assertIsNone(node.get_left())
        self.assertIsNone(node.get_right())

        node.set_code('01')
        self.assertEqual(node.get_code(), '01')

    def test_get_value(self):
        node = HuffmanNode('a', 1)
        self.assertEqual(node.get_letter(), 'a')
        self.assertEqual(node.get_frequency(), 1)
        self.assertIsNone(node.get_code())
        self.assertIsNone(node.get_left())
        self.assertIsNone(node.get_right())

        self.assertEqual(node.get_value(), node)

    def test_string(self):
        node = HuffmanNode('a', 1)
        node.set_code('01')
        self.assertEqual(node.get_letter(), 'a')
        self.assertEqual(node.get_frequency(), 1)
        self.assertEqual(node.get_code(), '01')
        self.assertEqual(node.__repr__(), 'a 1 01')

    def test_equality(self):
        node1 = HuffmanNode('a', 1)
        node1.set_code('01')

        node2 = HuffmanNode('a', 1)
        node2.set_code('000')

        self.assertEqual(node1, node2)
        self.assertEqual(node1.__hash__(), node2.__hash__())

    def test_not_equal(self):
        node1 = HuffmanNode('a', 1)
        node1.set_code('01')

        node2 = HuffmanNode('b', 1)
        node2.set_code('01')

        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1.__hash__(), node2.__hash__())

    def test_less_than(self):
        node1 = HuffmanNode('a', 1)
        node2 = HuffmanNode('b', 8)
        self.assertTrue(node1 < node2)

        node1 = HuffmanNode('a', 1)
        node2 = HuffmanNode('b', 1)
        self.assertTrue(node2 < node1)

    def test_bigger_than(self):
        node1 = HuffmanNode('a', 1)
        node2 = HuffmanNode('b', 8)
        self.assertTrue(node2 > node1)

        node1 = HuffmanNode('b', 1)
        node2 = HuffmanNode('a', 8)
        self.assertTrue(node2 > node1)


if __name__ == '__main__':
    unittest.main()
