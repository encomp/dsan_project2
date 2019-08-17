import unittest
from project2.collections.BinaryTree import BinaryTree


class BinaryTreeTest(unittest.TestCase):

    def test_new_tree(self):
        bt = BinaryTree()
        self.assertTrue(bt.insert(10))
        self.assertTrue(bt.insert(4))
        self.assertTrue(bt.insert(7))
        self.assertTrue(bt.insert(2))
        self.assertTrue(bt.insert(20))

if __name__ == '__main__':
    unittest.main()
