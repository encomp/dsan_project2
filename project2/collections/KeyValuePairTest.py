import unittest
from project2.collections.KeyValuePair import KeyValuePair


class KeyValuePairTestCase(unittest.TestCase):

    def test_new_kvp(self):
        kvp = KeyValuePair("Hola", "Mundo")
        self.assertEqual(kvp.get_key(), "Hola")
        self.assertEqual(kvp.get_value(), "Mundo")

    def test_set_key(self):
        kvp = KeyValuePair("Hola", "Mundo")
        kvp.set_key(1)
        self.assertEqual(kvp.get_key(), 1)
        self.assertEqual(kvp.get_value(), "Mundo")

    def test_set_value(self):
        kvp = KeyValuePair("Hola", "Mundo")
        kvp.set_value(1)
        self.assertEqual(kvp.get_key(), "Hola")
        self.assertEqual(kvp.get_value(), 1)

    def test_equal(self):
        kvp1 = KeyValuePair("Hola", "Mundo")
        kvp2 = KeyValuePair("Hola", "World")

        self.assertEqual(kvp1.get_key(), "Hola")
        self.assertEqual(kvp1.get_value(), "Mundo")
        self.assertEqual(kvp2.get_key(), "Hola")
        self.assertEqual(kvp2.get_value(), "World")

        self.assertEqual(kvp1, kvp2)
        self.assertEqual(kvp1.__hash__(), kvp2.__hash__())

    def test_not_equal(self):
        kvp1 = KeyValuePair("Hola", "Mundo")
        kvp2 = KeyValuePair("Hello", "World")

        self.assertEqual(kvp1.get_key(), "Hola")
        self.assertEqual(kvp1.get_value(), "Mundo")
        self.assertEqual(kvp2.get_key(), "Hello")
        self.assertEqual(kvp2.get_value(), "World")

        self.assertNotEqual(kvp1, kvp2)
        self.assertNotEqual(kvp1.__hash__(), kvp2.__hash__())

    def test_string(self):
        kvp = KeyValuePair("Hola", "Mundo")

        self.assertEqual(kvp.get_key(), "Hola")
        self.assertEqual(kvp.get_value(), "Mundo")
        self.assertEqual(kvp.__repr__(), "(Hola, Mundo)")


if __name__ == '__main__':
    unittest.main()
