class Student(object):
    def __init__(self, user_email):
        self.user_email = user_email

    def some_action(self):
        return "A student with " + self.user_email + " is attending a seminar"


class Teacher(object):
    def __init__(self, user_email):
        self.user_email = user_email

    def some_action(self):
        return "A teacher with " + self.user_email + " is taking a seminar"


class Administrator(object):
    def __init__(self, user_email):
        self.user_email = user_email

    def some_action(self):
        return "An administrator with " + self.user_email + \
               " is arranging a seminar"


class User(object):
    def __init__(self, user_email, user_type):
        self.user_email = user_email
        self.user_type = user_type.lower()

    def factory(self):
        if self.user_type == "student":
            return Student(user_email=self.user_email)
        elif self.user_type == "teacher":
            return Teacher(user_email=self.user_email)
        elif self.user_type == "administrator":
            return Administrator(user_email=self.user_email)
        raise ValueError("User type is not valid")


if __name__ == '__main__':
    try:
        user1 = User("dummy1@example.com", "Student").factory()
        print(user1.some_action())

        user2 = User("dummy2@example.com", "Teacher").factory()
        print(user2.some_action())

        user3 = User("dummy3@example.com", "Administrator").factory()
        print(user3.some_action())

        user4 = User("dummy4@example.com", "Guest").factory()
        print(user4.some_action())
    except Exception as e:
        print(str(e))
