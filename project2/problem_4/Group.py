

class Group:
    def __init__(self, _name):
        self.__name = _name
        self.__groups = []
        self.__users = []

    def add_group(self, group):
        self.__groups.append(group)

    def add_user(self, user):
        self.__users.append(user)

    def get_groups(self):
        return self.__groups

    def get_users(self):
        return self.__users

    def get_name(self):
        return self.__name

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.__name == other.__name

    def __hash__(self):
        return hash(self.__name)

    def __repr__(self):
        return "{}\n\tgroups: {}\n\tusers: {}".format(self.__name, self.__groups, self.__users)

    @staticmethod
    def is_user_in_group(user, group) -> bool:
        """
        Return True if user is in the group, False otherwise.

        Args:
          user(str): user name/id
          group(class:Group): group to check user membership against
        """
        if user is None or group is None:
            return False
        if user in group.get_users():
            return True
        for tmp_group in group.get_groups():
            if Group.is_user_in_group(user, tmp_group):
                return True
        return False
