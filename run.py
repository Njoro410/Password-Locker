#!/usr/bin/env python3.8

# change the mode (chmod +x run.py) in terminal

from user import User
from credentials import Credential

#create a new user
def create_user(name,email,password):
    new_user = User(name,email,password)
    return new_user

#create new credential
def create_credential(account,uname,pword,mail):
    new_credential = Credential(account,uname,pword,mail)
    return new_credential

def save_user(user: User):
    """
    method that saves new user
    """
    user.save_user()

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