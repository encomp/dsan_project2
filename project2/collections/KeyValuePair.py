

class KeyValuePair:

    def __init__(self, key, value=None):
        self.__key = key
        self.__value = value

    def set_value(self, value):
        self.__value = value
        return

    def get_value(self):
        return self.__value

    def set_key(self, key):
        self.__key = key
        return

    def get_key(self):
        return self.__key

    def __repr__(self):
        return "({}, {})".format(self.__key, self.__value)

    def __hash__(self):
        return hash(self.__key)

    def __eq__(self, other: object) -> bool:
        return self.__class__ == other.__class__ and self.__key == other.__key