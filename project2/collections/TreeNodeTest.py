import unittest
from project2.collections.TreeNode import TreeNode


class TreeNodeTest(unittest.TestCase):

    def test_new_tree_node(self):
        node = TreeNode("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertIsNone(node.get_right())
        self.assertIsNone(node.get_left())
        self.assertTrue(node.is_leaf())

    def test_set_right(self):
        other = TreeNode("Mundo")
        self.assertEqual(other.get_value(), "Mundo")

        node = TreeNode("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertIsNone(node.get_right())
        self.assertIsNone(node.get_left())
        self.assertTrue(node.is_leaf())

        node.set_right(other)
        self.assertEqual(node.get_right(), other)
        self.assertIsNone(node.get_left())
        self.assertFalse(node.is_leaf())

    def test_set_left(self):
        other = TreeNode("Mundo")
        self.assertEqual(other.get_value(), "Mundo")

        node = TreeNode("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertIsNone(node.get_right())
        self.assertIsNone(node.get_left())
        self.assertTrue(node.is_leaf())

        node.set_left(other)
        self.assertEqual(node.get_left(), other)
        self.assertIsNone(node.get_right())
        self.assertFalse(node.is_leaf())

    def test_string(self):
        node = TreeNode("Hola")
        self.assertEqual(node.get_value(), "Hola")
        self.assertEqual(node.__repr__(), "Hola")

if __name__ == '__main__':
    unittest.main()
