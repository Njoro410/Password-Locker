from genericpath import exists
import unittest
from psutil import users
import pyperclip

from user import User
# import required modules


class TestUser(unittest.TestCase):  # import Testcase module to show that this is a test class

    def setUp(self):  # initialize appropriate values before running tests
        self.new_user = User("Brayo", "example@mail.com", "abc123",)

    def tearDown(self):  # method called to initialize everything back to base after each test case
        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name, "Brayo")
        self.assertEqual(self.new_user.email, "example@mail.com")
        self.assertEqual(self.new_user.password, "abc123")

    def test_save_user(self):
        """Test to save a new user object"""
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user(self):
        """Test find user"""
        self.new_user.save_user()
        test_user = User("Brayo","example@mail.com","abc123")
        test_user.save_user()

        found_user = User.find_user_by_email("example@mail.com")

        self.assertEqual(found_user.user_name, test_user.user_name)

    def test_user_exists(self):
        """Test to check whether user object exists"""
        self.new_user.save_user()
        test_user = User("Brayo","example@mail.com","abc123")
        test_user.save_user()

        exists = User.user_exists(test_user.email,test_user.password)
        self.assertTrue(exists)


if __name__ == '__main__':
    unittest.main()
