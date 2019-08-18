import unittest

from project2.problem_1.LruCache import LruCache


class LruCacheTestCase(unittest.TestCase):

    def test_new_cache(self):
        lru = LruCache(5)
        self.assertTrue(lru.set(1, 1))
        self.assertTrue(lru.set(2, 2))
        self.assertTrue(lru.set(3, 3))
        self.assertTrue(lru.set(4, 4))
        self.assertEqual(lru.capacity(), 5)
        self.assertEqual(lru.size(), 4)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

    def test_full_cache(self):
        lru = LruCache(3)
        self.assertTrue(lru.set(1, 1))
        self.assertTrue(lru.set(2, 2))
        self.assertTrue(lru.set(3, 3))
        self.assertEqual(lru.capacity(), 3)
        self.assertEqual(lru.size(), 3)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)

    def test_remove_lru_max_capacity(self):
        lru = LruCache(3)
        self.assertTrue(lru.set(1, 1))
        self.assertTrue(lru.set(2, 2))
        self.assertTrue(lru.set(3, 3))
        self.assertEqual(lru.capacity(), 3)
        self.assertEqual(lru.size(), 3)

        self.assertTrue(lru.set(4, 4))
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

    def test_replace_value(self):
        lru = LruCache(3)
        self.assertTrue(lru.set(1, 1))
        self.assertTrue(lru.set(2, 2))
        self.assertTrue(lru.set(3, 3))
        self.assertEqual(lru.capacity(), 3)
        self.assertEqual(lru.size(), 3)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)

        self.assertTrue(lru.set(1, 10))
        self.assertEqual(lru.get(1), 10)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)

    def test_new_cache_with_default_capacity(self):
        lru = LruCache()
        self.assertTrue(lru.set(1, 1))
        self.assertTrue(lru.set(2, 2))
        self.assertTrue(lru.set(3, 3))
        self.assertTrue(lru.set(4, 4))
        self.assertTrue(lru.set(5, 5))
        self.assertEqual(lru.capacity(), 10)
        self.assertEqual(lru.size(), 5)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.get(2), 2)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)
        self.assertEqual(lru.get(5), 5)

    def test_set_element_with_none_key(self):
        lru = LruCache(3)
        self.assertFalse(lru.set(None, 5))
        self.assertEqual(lru.capacity(), 3)
        self.assertEqual(lru.size(), 0)

    def test_get_element_with_none_key(self):
        lru = LruCache(3)
        self.assertEqual(lru.get(None), -1)

    def test_cache_with_zero_capacity(self):
        lru = LruCache(0)
        self.assertEqual(lru.capacity(), 0)
        self.assertEqual(lru.size(), 0)
        self.assertEqual(lru.get(None), -1)
        self.assertFalse(lru.set(1, 5))
        self.assertEqual(lru.size(), 0)

if __name__ == '__main__':
    unittest.main()
