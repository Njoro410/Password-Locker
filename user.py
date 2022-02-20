import string

from sqlalchemy import Integer


class User:
    """
    This class' purpose is to create instances of User
    """

    #user_list = [] #this creates an empty class of users

    def __init__(self,user_name:string, email:string ,password:string):
        """
        this method will define User class properties

        :param user_name:
        :email:
        :password:
        """
        self.user_name = user_name
        self.email = email
        self.password = password

    def save_user(self):
        User.user_list.append(self)
