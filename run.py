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


