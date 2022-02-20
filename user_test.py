import unittest
import pyperclip

from user import User
#import required modules

class TestUser(unittest.TestCase): #import Testcase module to show that this is a test class

    def setUp(self): #initialize appropriate values before running tests
        self.new_user = User("First","secret word","example@mail.com")

    