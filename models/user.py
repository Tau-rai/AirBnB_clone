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
        if kwargs:
            self.email = kwargs.get('email', "")
            self.password = kwargs.get('password', "")
            self.first_name = kwargs.get('first_name', "")
            self.last_name = kwargs.get('last_name', "")
        else:
            self.email = ""
            self.password = ""
            self.first_name = ""
            self.last_name = ""
