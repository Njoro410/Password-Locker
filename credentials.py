import pyperclip
import string
import secrets


class Credential:
    """
    this class will create instances of credentials
    """

    credential_list = []  # creates an empty list of credentials

    def __init__(self, account_name, user_details, secret_key, email):
        """
        this method will define credential class properties

        :param account_name:
        :param user_details:
        :param password:
        :param email:
        """
        self.account_name = account_name
        self.user_details = user_details
        self.secret_key = secret_key
        self.email = email

    def save_credential(self):
        Credential.credential_list.append(self)

    def delete_credential(self):
        Credential.credential_list.remove(self)

    @classmethod
    def find_credential_by_account_name(cls, account_name):
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def credential_exists(cls, account_name):
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        return cls.credential_list
