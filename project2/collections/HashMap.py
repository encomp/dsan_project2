from project2.collections.DoubleLinkedList import DoubleLinkedList
from project2.collections.KeyValuePair import KeyValuePair


class HashMap:

    def __init__(self, capacity=10):
        self.__buckets = [DoubleLinkedList() for _ in range(capacity)]
        self.__capacity = capacity
        self.__size = 0
        return

    def size(self):
        return self.__size

    def __find(self, key):
        if self.size() > 0 or key is None:
            index = self.__bucket_index(key)
            dll = self.__buckets[index]
            return dll.find_value(KeyValuePair(key))
        return None

    def put(self, key, value):
        if key is not None:
            key_value_pair = self.__find(key)
            if key_value_pair:
                key_value_pair.set_value(value)
                return True
            index = self.__bucket_index(key)
            dll = self.__buckets[index]
            dll.insert(KeyValuePair(key, value))
            self.__size += 1
            return True
        return False

    def get(self, key):
        if self.size() > 0 or key is None:
            key_value_pair = self.__find(key)
            if key_value_pair is not None:
                return key_value_pair.get_value()
        return None

    def remove(self, key):
        if self.size() > 0 or key is None:
            index = self.__bucket_index(key)
            dll = self.__buckets[index]
            if dll.remove(KeyValuePair(key)):
                self.__size -= 1
                return True
        return False

    def __bucket_index(self, key):
        return hash(key) % self.__capacity

    def __iter__(self):
        for dll in self.__buckets:
            if dll.size() > 0:
                for kvp in dll:
                    yield kvp.get_key(), kvp.get_value()

    def __repr__(self):
        return "HashMap: [{}]".format(", ".join(str(x) for x in self))