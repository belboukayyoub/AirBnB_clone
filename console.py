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

    def do_show(self, line):
        """show: show [Class] [ID]"""
        line = line.split()
        data = storage.all()
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(line[0], line[1])
            if key not in data:
                print("** no instance found **")
            else:
                print(data[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            line = line.split()
            if line[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(line) == 1:
                print("** instance id missing **")
            else:
                data = storage.all()
                key = "{}.{}".format(line[0], line[1])
                if key not in data:
                    print("** no instance found **")
                else:
                    del data[key]
                    storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name.
        """
        if line != "":
            line = line.split()
            if line[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                data = [
                    str(obj)
                    for key, obj in storage.all().items()
                    if type(obj).__name__ == line[0]
                ]
                print(data)
        else:
            data = [str(obj) for key, obj in storage.all().items()]
            print(data)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
