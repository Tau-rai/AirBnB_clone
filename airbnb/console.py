#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for a simple command-line interpreter.

    Attributes:
        prompt (str): The custom prompt for the command-line.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Args:
            arg (str): Any arguments provided with the command.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.

        Args:
            arg (str): Any arguments provided with the command.

        Returns:
            bool: True to exit the program.
        """
        
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

