#!/usr/bin/python3

# file_storage.py
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r+b') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        obj_instance = User(**value)
                    elif class_name == "State":
                        obj_instance = State(**value)
                    elif class_name == "City":
                        obj_instance = City(**value)
                    elif class_name == "Amenity":
                        obj_instance = Amenity(**value)
                    elif class_name == "Place":
                        obj_instance = Place(**value)
                    elif class_name == "Review":
                        obj_instance = Review(**value)
                    else:
                        obj_class = globals()[class_name]
                        obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass

# Create an instance of FileStorage
storage = FileStorage()
storage.reload()

