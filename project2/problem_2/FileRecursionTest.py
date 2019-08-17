import unittest

from project2.problem_2.FileRecursion import find_files


class FileRecursionTest(unittest.TestCase):

    def test_suffix_c(self):
        expected = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c',
                    './testdir/subdir1/a.c']
        self.assertTrue(find_files(".c", "."), expected)

    def test_suffix_h(self):
        expected = ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h',
                    './testdir/subdir1/a.h']
        self.assertTrue(find_files(".h", "."), expected)

    def test_none_path(self):
        self.assertIsNone(find_files(".g", None))
        self.assertIsNone(find_files(".g", ""))

    def test_empty_result(self):
        self.assertEqual(find_files(".java", "."), [])


if __name__ == '__main__':
    unittest.main()
