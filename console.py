#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter
"""


import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    v_cl = ["User", "State", "City", "Amenity", "Place", "Review", "BaseModel"]

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

    def do_create(self, arg):
        """Creates a new instance of a specified class\
                and saves it to a JSON file, then prints the id.

        Usage: create <class name>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.v_cl:
            print("** class doesn't exist **")
        else:
            try:
                new_instance = globals()[args[0]]()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.v_cl:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            instance = storage.all().get(key)
            if instance is None:
                print("** no instance found **")
            else:
                print(instance.__str__())

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id.
            The change is saved into the JSON file.

        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.v_cl:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                cls_name = args[0]
                instance_id = args[1]
                key = "{}.{}".format(cls_name, instance_id)
                objects = storage.all()
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")
            except Exception:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based\
                or not on the class name.

        Usage: all [<class name>]
        """
        args = shlex.split(arg)
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.v_cl:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            output = []
            for key, obj in objects.items():
                if key.startswith(class_name):
                    output.append(str(obj))
            print(output)

    def do_update(self, line):
        """Updates an instance based on the class name and id
        """
        args = line.split()
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in self.v_cl:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in storage.all():
                print("** no instance found **")
            else:
                instance = storage.all()[key]
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
                storage.save()

    def default(self, line):
        """Retrieves all instances of a class

        Usage: <classname>.all()
        """
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            command = args[1]
            if command == "all()":
                self.do_all(class_name)
            elif command == "count()":
                count = 0
                for obj in storage.all().values():
                    if obj.__class__.__name__ == class_name:
                        count += 1
                print(count)
            elif "show(" in command and ")" in command:
                # extract id from the command
                id = command[5:-1]
                key = class_name + "." + id
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
