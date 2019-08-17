import hashlib
from datetime import datetime


class Block:

    def __init__(self, data, previous_hash=0, timestamp=datetime.utcnow()):
        self.__timestamp = timestamp
        self.__data = data
        self.__previous_hash = previous_hash
        self.__hash = self.__calc_hash()

    def __calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.__data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_timestamp(self):
        return self.__timestamp

    def get_data(self):
        return self.__data

    def get_previous_hash(self):
        return self.__previous_hash

    def get_hash(self):
        return self.__hash

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.__timestamp, self.__data, self.__previous_hash, self.__hash)
