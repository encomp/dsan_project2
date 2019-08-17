import unittest
from project2.collections.HashMap import HashMap


class HashMapTestCase(unittest.TestCase):

    def setUp(self):
        self.__items = [1, 2, 3, 4]
        self.__hm = HashMap()

    def test_size(self):
        self.assertEqual(self.__hm.size(), 0)

    def test_put_one_item(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)

    def test_put_same_item_multiple_times(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)

        self.assertTrue(self.__hm.put(123, 123))
        self.assertTrue(self.__hm.put(123, 123))
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)

    def test_put_one_item_with_no_key(self):
        self.assertFalse(self.__hm.put(None, 123))
        self.assertEqual(self.__hm.size(), 0)

    def test_get_one_item(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)
        self.assertEqual(self.__hm.get(123), 123)

    def test_get_one_item_is_not_there_on_empty_hm(self):
        self.assertEqual(self.__hm.size(), 0)
        self.assertIsNone(self.__hm.get(124))

    def test_get_one_item_is_not_there(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)
        self.assertIsNone(self.__hm.get(124))

    def test_get_one_item_with_no_key(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)
        self.assertFalse(self.__hm.get(None))

    def test_remove_one_item(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)

        self.assertTrue(self.__hm.remove(123))
        self.assertEqual(self.__hm.size(), 0)

    def test_remove_one_item_is_not_there(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)

        self.assertFalse(self.__hm.remove(125))
        self.assertEqual(self.__hm.size(), 1)

    def test_remove_one_item_is_not_there_on_empty_hm(self):
        self.assertEqual(self.__hm.size(), 0)
        self.assertFalse(self.__hm.remove(125))

    def test_remove_one_item_with_no_key(self):
        self.__hm.put(123, 123)
        self.assertEqual(self.__hm.size(), 1)

        self.assertFalse(self.__hm.remove(None))
        self.assertEqual(self.__hm.size(), 1)

    def test_multiple_operations(self):
        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 1)
        self.assertTrue(self.__hm.put(777, 777))
        self.assertEqual(self.__hm.size(), 2)
        self.assertTrue(self.__hm.put(2, 2))
        self.assertEqual(self.__hm.size(), 3)

        self.assertTrue(self.__hm.remove(123))
        self.assertEqual(self.__hm.size(), 2)

        self.assertTrue(self.__hm.put(123, 123))
        self.assertEqual(self.__hm.size(), 3)

        self.assertEqual(self.__hm.get(2), 2)
        self.assertEqual(self.__hm.size(), 3)

        self.assertFalse(self.__hm.remove(None))
        self.assertTrue(self.__hm.remove(2))
        self.assertFalse(self.__hm.remove(9))
        self.assertTrue(self.__hm.remove(123))
        self.assertFalse(self.__hm.remove(1))
        self.assertTrue(self.__hm.remove(777))
        self.assertEqual(self.__hm.size(), 0)



if __name__ == '__main__':
    unittest.main()
