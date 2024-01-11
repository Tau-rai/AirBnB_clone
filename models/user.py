#!/usr/bin/python3
"""
This module contains a class that inherits from BaseModel
"""


from models.base_model import BaseModel



class User(BaseModel):
    """
    User class that inherits from BaseModel
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance
        """
        user_dict = super().to_dict()
        user_dict['email'] = self.email
        user_dict['password'] = self.password
        user_dict['first_name'] = self.first_name
        user_dict['last_name'] = self.last_name
        return user_dict