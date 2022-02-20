#!/usr/bin/env python3.8

# change the mode (chmod +x run.py) in terminal

import string
import secrets
from user import User
from credentials import Credential

# create a new user


def create_user(name, email, password):
    new_user = User(name, email, password)
    return new_user

# create new credential


def create_credential(account, uname, pword, mail):
    new_credential = Credential(account, uname, pword, mail)
    return new_credential


def save_user(user: User):
    """
    method that saves new user
    """
    user.save_user()


def check_existing_user(email, password):
    return User.user_exists(email, password)


def find_user(email):
    return User.find_user_by_email(email)


def save_credential(cred: Credential):
    """
    method that saves new credentials
    """
    cred.save_credential()


def delete_credential(cred: Credential):
    """
    method that deletes a credential
    """
    cred.delete_credential()


def locate_credential(account):
    """
    method that returns searched credential objects
    """
    return Credential.find_credential_by_account_name(account)


def credential_exists(account):
    """
    method that returns a boolean after checking credential
    """
    return Credential.credential_exists(account)


def display_credentials():
    """
    methid to returns all available credentials
    """
    return Credential.display_credentials()


def main():
    print("Howdy,Welcome to Password Locker, What's your name")
    user_name = input()

    print(f"Hey {user_name}. Do you have an account?(Y - yes, N - no)")
    print('*'*10)

    while True:

        short_code = input().upper()
        if short_code == 'N':
            print("Enter your details to create an account")
            print("*"*20)

            print("----Create a username----")
            name = input()

            print("----What's your email----")
            mail = input()

            print("----Set a new password----")
            passy = input()

            save_user(create_user(name, mail, passy))
            print('\n')
            print(f"Hooray new user >>{name}<< with email >>{mail}<< created")
            print('\n')
            print("****please press Y to log in****")

        elif short_code == 'Y':
            print("Enter your details to log in:")
            print("*"*20)

            print("****What's your email****")
            mail = input()

            print("****What's your password****")
            passy = input()

            if check_existing_user(mail, passy):
                search_user = find_user(mail)
                print('*'*20)

                print(f"Hello {search_user.user_name}")
                print("Navigate with these short codes: >>SE<< store existing credential,>>FC<< Find a credential, >>SN<< store new credential, >>VW<<  view credentials, >>DEL<< delete a credential,>>EX<< exit application,")
            else:
                print("****Oh Oh, Please input correct details****")
                print("*****Press Y/y to login again or  N/n to create an account*****")

        elif short_code == 'SE':
            print("***Create Existing Credential***")
            print("-"*20)

            print("Which account is this credential,eg,fb,twitter,insta")
            account = input()

            print("Username for this credential")
            uname = input()

            print("What is this credential's password")
            pword = input()

            print("What's this credential's Email")
            mail = input()

            save_credential(create_credential(account, uname, pword, mail))
            print('\n')
            print(
                f"Existing Credential Created \n Account: {account} \n Username: {uname} \n Password: {pword} \n Email: {mail}")
            print("Navigate with these short codes: >>SE<< store existing credential,>>FC<< Find a credential, >>SN<< store new credential, >>VW<<  view credentials, >>DEL<< delete a credential,>>EX<< exit application,")

        elif short_code == 'SN':

            print("***Create New Credential***")
            print("-"*20)

            print("Which account is this credential eg. twitter,fb,insta")
            account = input()

            print("Username for this credential")
            uname = input()

            print("What's this credential's Email")
            mail = input()

            print(
                "Press AP - to get an auto generated password(recommended) or MP- to input your own password")

            short_code2 = input().upper()
            if short_code2 == "AP":
                length = 10
                random_password = ''.join(secrets.choice(
                    string.ascii_letters + string.digits) for i in range(length))
                pword = str(random_password)
            elif short_code2 == "MP":
                print("What is this credential's password")
                pword = input()

            save_credential(create_credential(account, uname, pword, mail))
            print('\n')
            print(
                f"New Credential Created \n Account: {account} \n Username: {uname} \n Password: {pword} \n Email: {mail}")
            print("Navigate with these short codes: >>SE<< store existing credential,>>FC<< Find a credential, >>SN<< store new credential, >>VW<<  view credentials, >>DEL<< delete a credential,>>EX<< exit application,")

        elif short_code == 'VW':
            """Method to view a list of credentials"""

            if display_credentials():
                print("Your credentials are as below")
                print('\n')

                for credential in display_credentials():
                    print(
                        f"{credential.account_name} \n {credential.user_details} \n {credential.secret_key} \n {credential.email}")

                print('\n')
            else:

                print('\n')
                print("Ooops, Looks like you don't have any credentials")
                print('\n')
                print("Navigate with these short codes: >>SE<< store existing credential,>>FC<< Find a credential, >>SN<< store new credential, >>VW<<  view credentials, >>DEL<< delete a credential,>>EX<< exit application,")

        elif short_code == "FC":
            """Credential search implementation"""

            print("Enter account name for credential you are looking for")

            query_name = input()
            if credential_exists(query_name):
                search_credential = locate_credential(query_name)
                print(f"Account Name:-----{search_credential.account_name}")
                print(f"User Name:-----{search_credential.user_details}")
                print(f"Password:-----{search_credential.secret_key}")
                print(f"Email:-----{search_credential.email}")
            else:
                print(";-( credential does not exist")
                print("Navigate with these short codes: >>SE<< store existing credential,>>FC<< Find a credential, >>SN<< store new credential, >>VW<<  view credentials, >>DEL<< delete a credential,>>EX<< exit application,")

        elif short_code == 'DEL':
            """Below is a method to delete a password"""

            print("Enter account name for credential to delete")
            delete_query = input()
            if credential_exists(delete_query):
                delete_credential(credential)
                print("credential deleted successfully")
            else:
                print("enter account name correctly")

                print("Navigate with these short codes: >>SE<< store existing credential,>>FC<< Find a credential, >>SN<< store new credential, >>VW<<  view credentials, >>DEL<< delete a credential,>>EX<< exit application,")
        elif short_code == 'EX':
            print("Thank You for using Password Locker")
            break
        else:
            print("Please use correct short code")


if __name__ == '__main__':
    main()
