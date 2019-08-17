import unittest
from project2.problem_2.FileRecursion import find_files


class FileRecursionTestCase(unittest.TestCase):

    def test_something(self):
        print(find_files(".c", "/Users/edgarrico/Downloads/testdir"))


if __name__ == '__main__':
    unittest.main()
