import unittest
from project2.collections.DoubleLinkedList import DoubleLinkedList
from project2.problem_6.ListOperations import union
from project2.problem_6.ListOperations import intersection


class ListOperationsTest(unittest.TestCase):

    def setUp(self):
        elements_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
        self.__list1 = DoubleLinkedList()
        for element in elements_1:
            self.__list1.insert(element)
        elements_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
        self.__list2 = DoubleLinkedList()
        for element in elements_2:
            self.__list2.insert(element)
        elements_3 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
        self.__list3 = DoubleLinkedList()
        for element in elements_3:
            self.__list3.insert(element)
        self.__list4 = DoubleLinkedList()
        elements_4 = [1, 7, 8, 9, 11, 21, 1]
        for element in elements_4:
            self.__list4.insert(element)

    def test_union_two_lists(self):
        lista = union(self.__list1, self.__list2)
        arr = self.__to_list(self.__list1)
        arr.extend(self.__to_list(self.__list2))
        self.__assert_dll(arr, lista)

        lista = union(self.__list3, self.__list4)
        arr = self.__to_list(self.__list3)
        arr.extend(self.__to_list(self.__list4))
        self.__assert_dll(arr, lista)

    def test_union_two_none_lists(self):
        lista = union(None, None)
        self.assertEqual(lista.size(), 0)

    def test_union_two_lists_with_first_as_none(self):
        lista = union(None, self.__list2)
        arr = self.__to_list(self.__list2)
        self.__assert_dll(arr, lista)

    def test_union_two_lists_with_second_as_none(self):
        lista = union(self.__list1, None)
        arr = self.__to_list(self.__list1)
        self.__assert_dll(arr, lista)

    def test_intersection_two_lists(self):
        lista = intersection(self.__list1, self.__list2)
        arr = [6, 4, 6, 21]
        self.__assert_dll(arr, lista)

        lista = intersection(self.__list3, self.__list4)
        arr = []
        self.__assert_dll(arr, lista)

    def test_intersection_two_none_lists(self):
        lista = intersection(None, None)
        self.assertEqual(lista.size(), 0)

    def __assert_dll(self, arr, llist):
        ll_arr = self.__to_list(llist)
        self.assertListEqual(arr, ll_arr)

    def __to_list(self, llist):
        arr = list()
        for element in llist:
            arr.append(element)
        return arr

if __name__ == '__main__':
    unittest.main()
