import string

from sqlalchemy import Integer


class User:
    """
    This class' purpose is to create instances of User
    """

    user_list = [] #this creates an empty class of users

    def __init__(self,user_name, email ,password):
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

    @classmethod
    def find_user_by_email(cls,email):
        for user in cls.user_list:
            if user.email == email:
                return user
        return False

    @classmethod
    def user_exists(cls, email,password):
        for user in cls.user_list:
            if user.email == email and user.password == password:
                return True

        return False
    
    # @classmethod
    # def password_exists(cls, password):
    #     for password in cls.user_list:
    #         if password.password == password:
    #             return True
        
    #     return False
    
