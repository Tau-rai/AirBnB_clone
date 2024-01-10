#!/usr/bin/python3
"""This module contains the base model class
"""
from datetime import datetime
import uuid
from __init__ import storage


class BaseModel:
    """
    class that defines all common attribute/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """Instatiates the public attributes of the class
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
 
    def __str__(self) -> str:
        """returns a string representation of the class

        Returns:
            str: string representation of the class
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the public attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dict containing all keys/values of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()

        return dict_copy
