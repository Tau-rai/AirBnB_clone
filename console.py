#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""


import cmd
import json
import models.base_model as BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """The command interpreter class
    """
    completekey = "tab"
    prompt = '(hbnb) '

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
        """
        Does nothing if an empty line is passed to the interprter
        """
        pass

    def do_create(self, line):
        """
        Creates an instance of BaseModel, saves it to JSON file and prints the id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] != "BaseModel":
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            self.storage.new(new_instance)
            self.storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
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
        elif args[0] != "BaseModel":
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
        """Prints all string representation of all instances based or not on class name
        """
        args = line.split()
        if len(args) == 0 or args[0] == "BaseModel":
            for instance in self.storage.all().values():
                print(instance.__str__())
        else: 
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] != "BaseModel":
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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
