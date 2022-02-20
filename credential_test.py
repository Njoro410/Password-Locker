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

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        """Test saving multiple credentials for multiple accounts"""
        self.new_credential.save_credential()
        test_credential = Credential("facebook","Joe Biden","1234abcd","example@yahoo.com")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)



if __name__ == '__main__':
    unittest.main()
