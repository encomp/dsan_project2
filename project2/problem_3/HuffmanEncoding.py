from queue import PriorityQueue

from project2.collections.BinaryTree import BinaryTree
from project2.collections.HuffmanNode import HuffmanNode


class HuffmanEncoding:

    def __init__(self):
        self.__ht = None
        self.__char_to_code = None

    def set_huffman_tree(self, huffman_tree):
        self.__ht = huffman_tree
        return

    def get_huffman_tree(self):
        return self.__ht

    def huffman_encoding(self, data):
        if data is None or len(data) == 0:
            return None
        self.__char_to_code = {}
        counters = self.__letter_counter(data)
        hc = self.__sorted_frequencies(counters)
        self.__ht = self.__build_tree(hc)
        self.__build_code(self.__ht.get_root(), '', self.__char_to_code)
        return self.__econde_input(data, self.__char_to_code)

    def __letter_counter(self, data):
        letter_counter = {}
        for item in data:
            if item in letter_counter:
                letter_counter[item] += 1
            else:
                letter_counter[item] = 1
        return letter_counter

    def __sorted_frequencies(self, counters):
        pq = PriorityQueue()
        for key in counters.keys():
            frequency = counters[key]
            hc = HuffmanNode(key, frequency)
            pq.put(hc)
        return pq

    def __build_tree(self, huffman_codes):
        nodes = 0
        while huffman_codes.qsize() > 1:
            left = huffman_codes.queue.pop(0)
            right = huffman_codes.queue.pop(0)
            parent = HuffmanNode('0', left.get_frequency() + right.get_frequency())
            parent.set_left(left)
            parent.set_right(right)
            huffman_codes.put(parent)
            nodes += 1
        if nodes == 0 and huffman_codes.qsize() == 1:
            left = huffman_codes.queue.pop(0)
            parent = HuffmanNode('0', left.get_frequency() + 1)
            parent.set_left(left)
            huffman_codes.put(parent)
        bt = BinaryTree(huffman_codes.queue.pop())
        return bt

    def __build_code(self, huffman_node, s, char_to_code):
        if huffman_node is None:
            return
        if not huffman_node.is_leaf():
            self.__build_code(huffman_node.get_left(), s + '0', char_to_code)
            self.__build_code(huffman_node.get_right(), s + '1', char_to_code)
        else:
            huffman_node.set_code(s)
            char_to_code[huffman_node.get_letter()] = s

    def __econde_input(self, data, char_to_code):
        msg = ""
        for letter in data:
            msg += char_to_code[letter]
        return msg

    def huffman_decoding(self, data):
        if data is None or len(data) == 0 or self.__ht is None:
            return None
        return self.__decode(self.__ht.get_root(), data, "")

    def __decode(self, root, data, msg):
        huffman_node = root
        for character in data:
            if character == '0':
                huffman_node = huffman_node.get_left()
            else:
                huffman_node = huffman_node.get_right()
            if huffman_node.is_leaf():
                msg += huffman_node.get_letter()
                huffman_node = root
        return msg

    def __repr__(self):
        if self.__ht is None:
            return super().__repr__()
        return self.__write_huffman_tree(self.__ht.get_root(), "")[:-1]

    def __write_huffman_tree(self, huffman_node, msg, new_msg=''):
        if huffman_node.is_leaf():
            return str(huffman_node.get_frequency()) + huffman_node.get_letter() + ":"
        new_msg += self.__write_huffman_tree(huffman_node.get_left(), msg)
        new_msg += self.__write_huffman_tree(huffman_node.get_right(), msg)
        return new_msg
