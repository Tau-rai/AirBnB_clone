#!/usr/bin/python3

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj


    @classmethod
    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    @classmethod
    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    class_instance = globals()[self.__class__.__name__](**value)
                    self.__objects[key] = class_instance
        except FileNotFoundError:
            pass

