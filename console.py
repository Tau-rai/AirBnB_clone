#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""


import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The command interpreter class
    """
    completekey = "tab"
    prompt = '(hbnb) '
    v_classes = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]
    
    def __init__(self):
        """Tracks the instances of the BaseModel from the Filestorage
        """
        super(HBNBCommand, self).__init__()
        self.cmdqueue = []
        self.storage = FileStorage()
        self.storage.reload()  # load existing instances from file
    
    def do_EOF(self, line):
        """EOF or Ctrl D will exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Does nothing if an empty line is passed to the interprter
        """
        pass

    def do_create(self, line):
        """Creates an instance of BaseModel, saves it to JSON file and prints the id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.v_classes:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                new_instance = BaseModel()
            elif args[0] == "User":
                new_instance = User()
            elif args[0] == "Place":
                new_instance = Place()
            elif args[0] == "State":
                new_instance = State()
            elif args[0] == "City":
                new_instance = City()
            elif args[0] == "Amenity":
                new_instance = Amenity()
            elif args[0] == "Review":
                new_instance = Review()
            self.storage.new(new_instance)
            self.storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.v_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instance = self.storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance.__str__())

    def do_destroy(self, line):
        """Deletes an instance based on class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.v_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in self.storage.all():
                print("** no instance found **")
            else:
                del self.storage.all()[key]
                self.storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        """
        args = line.split()
        if len(args) == 0:
            for instance in self.storage.all().values():
                print(instance.__str__())
        elif args[0] in self.v_classes:
            class_name = args[0]
            for instance in self.storage.all().values():
                if instance.__class__.__name__ == class_name:
                    print(instance.__str__())
        else: 
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.v_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in self.storage.all():
                print("** no instance found **")
            else:
                instance = self.storage.all()[key]
                attr_name = args[2]
                attr_val = args[3]

                # type cast the attr_value to appropriate type
                if attr_val.isdigit():
                    attr_val = int(attr_val)
                elif attr_val.replace('.', '', 1).isdigit():
                    attr_val = float(attr_val)
                else:
                    attr_val = str(attr_val)
                setattr(instance, attr_name, attr_val)
                self.storage.save()

    def default(self, line):
        """Retrieves all instances of a class by using: <classname>.all()

        Args:
            line (str): command line input
        """
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            command = args[1]
            if command == "all()":
                self.do_all(class_name)                 


if __name__ == '__main__':
    HBNBCommand().cmdloop()
