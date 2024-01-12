#!/usr/bin/python3
"""
This modele contains a class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class Review(BaseModel):
    """A class that inherits from the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.place_id = kwargs.get('place_id', "")
            self.user_id = kwargs.get('user_id', "")
            self.text = kwargs.get('text', "")
        else:

            self.place_id = ''
            self.user_id = ''
            self.text = ''
