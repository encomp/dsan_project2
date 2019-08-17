from functools import total_ordering
from project2.collections.TreeNode import TreeNode

@total_ordering
class HuffmanNode(TreeNode):

    def __init__(self, letter, frequency):
        self.__letter = letter
        self.__frequency = frequency
        self.__code = None
        self.set_left(None)
        self.set_right(None)

    def get_letter(self):
        return self.__letter

    def get_frequency(self):
        return self.__frequency

    def set_code(self, code):
        self.__code = code
        return

    def get_code(self):
        return self.__code

    def get_value(self):
        return self

    def __repr__(self):
        return "{} {} {}".format(self.__letter, self.__frequency, self.__code)

    def __hash__(self) -> int:
        return hash((self.__letter, self.__frequency))

    def __eq__(self, other: object) -> bool:
        return self.__class__ == other.__class__ \
               and self.__letter == other.__letter \
               and self.__frequency == other.__frequency

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.__class__ == other.__class__ \
               and (self.__frequency == other.__frequency and self.__letter > other.__letter) \
               or self.__frequency < other.__frequency

