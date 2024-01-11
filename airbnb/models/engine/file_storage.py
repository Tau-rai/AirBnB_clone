#!/usr/bin/python3

import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def save(self):
        with open(self.__file_path, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, file)

    @classmethod
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
