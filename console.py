#!/usr/bin/python3
"""
Command interpreter for AirBnB clone project
"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, _):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Function to handle EOF"""
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass  # Do nothing on an empty line

    def do_create(self, line):
        """Creates an instance."""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            b = storage.classes()[line]()
            b.save()
            print(b.id)

    def do_show(self, arg):
        """show: show [Class] [ID]"""
        arg = arg.split()
        data = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in data:
                print("** no instance found **")
            else:
                print(data[key])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
