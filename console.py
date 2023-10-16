#!/usr/bin/python3
"""
Command interpreter for AirBnB clone project
"""
import cmd


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
