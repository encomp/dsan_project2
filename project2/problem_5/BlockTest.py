import unittest
from datetime import datetime

from project2.problem_5.Block import Block


class BlockTest(unittest.TestCase):

    def test_new_block(self):
        time = datetime.utcnow()
        block = Block("Hola", 1, time)

        self.assertEqual(block.get_data(), "Hola")
        self.assertEqual(block.get_timestamp(), time)
        self.assertEqual(block.get_previous_hash(), 1)
        self.assertIsNotNone(block.get_hash())

    def test_new_default_block(self):
        block = Block("Hola")

        self.assertEqual(block.get_data(), "Hola")
        self.assertLessEqual(block.get_timestamp(), datetime.utcnow())
        self.assertIsNotNone(block.get_previous_hash())
        self.assertIsNotNone(block.get_hash())

    def test_new_block_with_previous_hash(self):
        block = Block("Hola", 1)

        self.assertEqual(block.get_data(), "Hola")
        self.assertLessEqual(block.get_timestamp(), datetime.utcnow())
        self.assertEqual(block.get_previous_hash(), 1)
        self.assertIsNotNone(block.get_hash())


if __name__ == '__main__':
    unittest.main()
