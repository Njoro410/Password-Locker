#!/usr/bin/env python3.8

# change the mode (chmod +x run.py) in terminal

from sqlalchemy import case
from user import User
from credentials import Credential

# create a new user


def create_user(name, email, password):
    new_user = User(name, email, password)
    return new_user

# create new credential


def create_credential(account, uname, pword, email):
    new_credential = Credential(account, uname, pword, email)
    return new_credential


def save_user(user: User):
    """
    method that saves new user
    """
    user.save_user()


def check_existing_user(email,password):
    return User.user_exists(email,password)


# def check_password(password):
#     return User.password_exists(password)


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

        # print("What would you like to do: se- store existing password, sn- store new password, vw - view credentials, del - delete a credential")
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

            if check_existing_user(mail,passy):
                search_user = find_user(mail)
                print('*'*20)

                print(f"Hello {search_user.user_name}")
                print("What would you like to do: >>se<< store existing credential, >>sn<< store new credential, >>vw<<  view credentials, >>del<< delete a credential")
            else:
                print("****Oh Oh, Please input correct details****")
                print("*****Press Y/y to login again or  N/y to create an account*****")


if __name__ == '__main__':
    main()
