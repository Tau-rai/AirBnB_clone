#!/usr/bin/python3

# console.py
import cmd
import shlex
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]  # Add other valid classes here

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it to a JSON file, then prints the id.

        Usage: create <class name>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            try:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.

        Usage: show <class name> <id>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                cls_name = args[0]
                instance_id = args[1]
                key = "{}.{}".format(cls_name, instance_id)
                objects = FileStorage().all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")
            except Exception:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id. The change is saved into the JSON file.

        Usage: destroy <class name> <id>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            try:
                cls_name = args[0]
                instance_id = args[1]
                key = "{}.{}".format(cls_name, instance_id)
                objects = FileStorage().all()
                if key in objects:
                    del objects[key]
                    FileStorage().save()
                else:
                    print("** no instance found **")
            except Exception:
                print("** instance id missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name.

        Usage: all [<class name>]
        """
        args = shlex.split(arg)
        objects = FileStorage().all()

        if not args:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating an attribute.
        The change is saved into the JSON file.

        Usage: update <class name> <id> <attribute name> <attribute value>
        """
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            if len(args) > 1:
                instance_id = args[1]
                key = "{}.{}".format(cls_name, instance_id)
                objects = FileStorage().all()
                if key in objects:
                    if len(args) > 2:
                        attr_name = args[2]
                        if len(args) > 3:
                            attr_value_str = args[3]
                            try:
                                attr_value = eval(attr_value_str)
                                if attr_name not in ["id", "created_at", "updated_at"]:
                                    setattr(objects[key], attr_name, attr_value)
                                    objects[key].save()
                                else:
                                    print("** can't update id, created_at, or updated_at **")
                            except (NameError, SyntaxError):
                                print("** value missing **")
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        except NameError:
            print("** class doesn't exist **")

    def emptyline(self):
        """Overrides repeating the last nonempty command after an empty line is entered"""
        pass

    def default(self, line):
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, arg):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exits the command interpreter when an EOF condition is passed"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()

