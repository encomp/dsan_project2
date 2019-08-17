import unittest
from project2.cache.LruCache import LruCache


class LruCacheTestCase(unittest.TestCase):

    def setUp(self):
        self.__lru = LruCache(5)

    def test_something(self):
        self.__lru.set(1, 1)
        self.__lru.set(2, 2)
        self.__lru.set(3, 3)
        self.__lru.set(4, 4)
        print(self.__lru)

        self.__lru.get(1)
        print(self.__lru)

        self.__lru.get(2)
        print(self.__lru)

        self.__lru.get(9)
        print(self.__lru)

        self.__lru.set(5, 5)
        print(self.__lru)

        self.__lru.set(6, 6)
        print(self.__lru)

        self.__lru.get(3)
        print(self.__lru)


if __name__ == '__main__':
    unittest.main()
