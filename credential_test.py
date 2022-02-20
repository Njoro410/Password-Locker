import unittest
import pyperclip

from credentials import Credential

#import necessary modules

class TestCredential(unittest.TestCase):

    def setUp(self):
        self.new_credential = Credential("twitter","obama","abcd1234","example@gmail.com")

    def tearDown(self):
        Credential.credential_list = []
    
    def test_init(self):
        self.assertEqual(self.new_credential.account_name, "twitter")
        self.assertEqual(self.new_credential.user_details, "obama")
        self.assertEqual(self.new_credential.secret_key, "abcd1234")
        self.assertEqual(self.new_credential.email, "example@gmail.com")


if __name__ == '__main__':
    unittest.main()
