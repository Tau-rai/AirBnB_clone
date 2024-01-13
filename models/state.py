#!/usr/bin/python3
"""
This modele contains a class that inherits from the BaseModel class
"""


from models.base_model import BaseModel
from datetime import datetime

class State(BaseModel):
    """A class that inherits from the BaseModel class
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if kwargs:
            self.name = kwargs.get('name', "")
        else:
            self.name = ''

        # Check if 'created_at' and 'updated_at' are strings before using strptime
        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")

