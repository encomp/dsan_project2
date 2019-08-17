import unittest

from project2.problem_4.Group import Group


class GroupTest(unittest.TestCase):

    def test_new_group(self):
        group = Group("group")
        self.assertEqual(group.get_name(), "group")
        self.assertEqual(group.get_groups(), [])
        self.assertEqual(group.get_users(), [])

    def test_equality(self):
        group1 = Group("group")
        self.assertEqual(group1.get_name(), "group")
        self.assertEqual(group1.get_groups(), [])
        self.assertEqual(group1.get_users(), [])

        group2 = Group("group")
        self.assertEqual(group2.get_name(), "group")
        self.assertEqual(group2.get_groups(), [])
        self.assertEqual(group2.get_users(), [])

        self.assertEqual(group1, group2)
        self.assertEqual(group1.__hash__(), group2.__hash__())

    def test_not_equal(self):
        group1 = Group("group")
        self.assertEqual(group1.get_name(), "group")
        self.assertEqual(group1.get_groups(), [])
        self.assertEqual(group1.get_users(), [])

        group2 = Group("group1")
        self.assertEqual(group2.get_name(), "group1")
        self.assertEqual(group2.get_groups(), [])
        self.assertEqual(group2.get_users(), [])

        self.assertNotEqual(group1, group2)
        self.assertNotEqual(group1.__hash__(), group2.__hash__())

    def test_parent_child(self):
        parent = Group("parent")
        self.assertEqual(parent.get_name(), "parent")
        self.assertEqual(parent.get_groups(), [])
        self.assertEqual(parent.get_users(), [])

        child = Group("child")
        self.assertEqual(child.get_name(), "child")
        self.assertEqual(child.get_groups(), [])
        self.assertEqual(child.get_users(), [])

        parent.add_group(child)
        self.assertEqual(parent.get_groups(), [child])

    def test_users(self):
        group = Group("parent")
        self.assertEqual(group.get_name(), "parent")
        self.assertEqual(group.get_groups(), [])
        self.assertEqual(group.get_users(), [])

        user = "user"
        group.add_user(user)
        self.assertEqual(group.get_users(), [user])

    def test_find_users(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        sub_child_user = "sub_child_user"
        sub_child.add_user(sub_child_user)
        child.add_group(sub_child)
        parent.add_group(child)
        self.assertTrue(Group.is_user_in_group(sub_child_user, parent))

    def test_find_multiple_users(self):
        parent = Group("parent")
        child = Group("child")
        sub_child = Group("subchild")
        parent_user = "parent_user"
        child_user = "child_user"
        sub_child_user = "sub_child_user"
        parent.add_user(parent_user)
        child.add_user(child_user)
        sub_child.add_user(sub_child_user)
        child.add_group(sub_child)
        parent.add_group(child)
        self.assertTrue(Group.is_user_in_group(sub_child_user, parent))
        self.assertTrue(Group.is_user_in_group(child_user, parent))
        self.assertTrue(Group.is_user_in_group(parent_user, parent))


if __name__ == '__main__':
    unittest.main()
