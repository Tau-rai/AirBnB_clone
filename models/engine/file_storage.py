#!/usr/bin/python3
"""
This module contains the FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances
"""


import json
import os


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
            if hasattr(value, 'to_dict') and callable(getattr(value, 'to_dict')):
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
                self.__objects = json.load(f)
