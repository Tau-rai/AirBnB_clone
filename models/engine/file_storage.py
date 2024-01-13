#!/usr/bin/python3
"""
This module contains the FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances
"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serialization and deserialization class
    """
    def __init__(self):
        """Instantiates the attribbutes of the class
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """Returns the dict __objects
        """
        return self.__objects

    def new(self, obj):
        """sets obejcts with th key id
        """
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes object to the JSON path
        """
        serialized_objs = {}

        for key, value in self.__objects.items():
            if hasattr(value, 'to_dict')\
                 and callable(getattr(value, 'to_dict')):
                serialized_objs[key] = value.to_dict()
            else:
                serialized_objs[key] = value

        with open(self.__file_path, 'w') as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """deserializes the JSON file to __objects
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
            for key in objects.keys():
                if objects[key]["__class__"] == "BaseModel":
                    self.__objects[key] = BaseModel(**objects[key])
                elif objects[key]["__class__"] == "User":
                    self.__objects[key] = User(**objects[key])
                elif objects[key]["__class__"] == "Place":
                    self.__objects[key] = Place(**objects[key])
                elif objects[key]["__class__"] == "State":
                    self.__objects[key] = State(**objects[key])
                elif objects[key]["__class__"] == "City":
                    self.__objects[key] = City(**objects[key])
                elif objects[key]["__class__"] == "Amenity":
                    self.__objects[key] = Amenity(**objects[key])
                elif objects[key]["__class__"] == "Review":
                    self.__objects[key] = Review(**objects[key])
