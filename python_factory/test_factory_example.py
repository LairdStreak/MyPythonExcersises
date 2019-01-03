import unittest
import factory_example


class TestUser(unittest.TestCase):
    def test_factory_for_student(self):
        user_email = "user@example.com"
        user_type = "Student"
        user = factory_example.User(user_email, user_type).factory()
        method_output = user.some_action()
        expected_output = "A student with " + user_email + \
                          " is attending a seminar"
        self.assertEqual(method_output, expected_output)

    def test_factory_for_teacher(self):
        user_email = "user@example.com"
        user_type = "Teacher"
        user = factory_example.User(user_email, user_type).factory()
        method_output = user.some_action()
        expected_output = "A teacher with " + user_email + \
                          " is taking a seminar"
        self.assertEqual(method_output, expected_output)

    def test_factory_for_administrator(self):
        user_email = "user@example.com"
        user_type = "Administrator"
        user = factory_example.User(user_email, user_type).factory()
        method_output = user.some_action()
        expected_output = "An administrator with " + user_email + \
                          " is arranging a seminar"
        self.assertEqual(method_output, expected_output)

    def test_factory_for_guest(self):
        user_email = "user@example.com"
        user_type = "Guest"
        user = factory_example.User(user_email, user_type)
        self.assertRaises(ValueError, user.factory)


if __name__ == '__main__':
    unittest.main()
