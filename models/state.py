#!/usr/bin/python3
"""
This modele contains a class that inherits from the BaseModel class
"""


from models.base_model import BaseModel


class State(BaseModel):
    """A class that inherits from the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ''