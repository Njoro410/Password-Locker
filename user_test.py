import unittest
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
        self.assertEqual(self.new_user.user_name,"Brayo")
        self.assertEqual(self.new_user.email,"example@mail.com")
        self.assertEqual(self.new_user.password,"abc123")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

if __name__ == '__main__':
    unittest.main()