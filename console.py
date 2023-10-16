#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self):
        """quit the program

        Returns:
            bool: ture to quite
        """
        return True

    def do_EOF(self, line):
        "Exit"
        return True

    def emptyline(self):
        pass  # Do nothing on an empty line


if __name__ == "__main__":
    HBNBCommand().cmdloop()
