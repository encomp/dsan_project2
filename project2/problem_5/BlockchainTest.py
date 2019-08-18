import unittest

from project2.problem_5.Blockchain import Blockchain


class BlockchainTest(unittest.TestCase):

    def setUp(self):
        self.__blockchain = Blockchain()
        self.__elements = ["Hola", "Mundo"]

    def test_new_blockchain(self):
        self.assertEqual(self.__blockchain.size(), 0)

    def test_add_one_element_blockchain(self):
        flag = self.__blockchain.add("Hola")

        self.assertTrue(flag)
        self.assertEqual(self.__blockchain.size(), 1)

    def test_add_two_element_blockchain(self):
        for element in self.__elements:
            self.assertTrue(self.__blockchain.add(element))

        i = 0
        for item in self.__blockchain:
            self.assertEqual(item.get_data(), self.__elements[i])
            i += 1
        self.assertEqual(self.__blockchain.size(), 2)
        print(self.__blockchain)

    def test_add_none_element_blockchain(self):
        self.assertFalse(self.__blockchain.add(None))
        self.assertEqual(self.__blockchain.size(), 0)

    def test_add_few_element_blockchain(self):
        elements = ["Hola", "Mundo", "Hello", "World", "Bonjour", "le monde", "Hallo", "Welt"]
        for element in elements:
            self.assertTrue(self.__blockchain.add(element))

        i = 0
        for item in self.__blockchain:
            self.assertEqual(item.get_data(), elements[i])
            i += 1
        self.assertEqual(self.__blockchain.size(), 8)
        print(self.__blockchain)


if __name__ == '__main__':
    unittest.main()
