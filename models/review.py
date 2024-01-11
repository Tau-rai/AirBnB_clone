#!/usr/bin/python3
"""
This modele contains a class that inherits from the BaseModel class
"""


from base_model import BaseModel


class Review(BaseModel):
    """A class that inherits from the BaseModel class
    """
    place_id = ''
    user_id = ''
    text = ''