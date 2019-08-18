import unittest

from project2.problem_3.HuffmanEncoding import HuffmanEncoding


class HuffmanEncodingTest(unittest.TestCase):

    def setUp(self) -> None:
        self.__encoder = HuffmanEncoding()

    def test_encode_decode_mississippi(self):
        encoded = self.__encoder.huffman_encoding("mississippi")
        self.assertEqual(encoded, "100110011001110110111")

        decoded = self.__encoder.huffman_decoding("100110011001110110111")
        self.assertEqual(decoded, "mississippi")

    def test_encode_decode_case_sensitive(self):
        encoded = self.__encoder.huffman_encoding("Edgar")
        self.assertEqual(encoded, '010011110110')

        decoded = self.__encoder.huffman_decoding('010011110110')
        self.assertEqual(decoded, "Edgar")

    def test_encode_none(self):
        encoded = self.__encoder.huffman_encoding(None)
        self.assertIsNone(encoded)

    def test_decode_none(self):
        decoded = self.__encoder.huffman_decoding(None)
        self.assertIsNone(decoded)

    def test_decode_none_with_empty_tree(self):
        decoded = self.__encoder.huffman_decoding("001011101110")
        self.assertIsNone(decoded)

    def test_encode_decode_tree(self):
        encoded = self.__encoder.huffman_encoding("AAA")
        self.assertEqual(encoded, "000")

        decoded = self.__encoder.huffman_decoding("000")
        self.assertEqual(decoded, "AAA")


if __name__ == '__main__':
    unittest.main()
