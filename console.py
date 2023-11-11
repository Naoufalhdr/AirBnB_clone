#!/usr/bin/python3
"""The console"""
import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


def custom_split(input_string):
    """
    Splits a given input string into a list of words, considering spaces as
    delimiters. Handles cases where words are enclosed in double quotes,
    treating them as single entities.

    Parameters:
    - input_string (str): The input string to be split.

    Returns:
    - list: A list of words extracted from the input string.

    Example:
    >>>custom_split('This is a "sample string" with spaces')
    ['This', 'is', 'a', 'sample string', 'with', 'spaces']
    """
    words = []
    in_quote = False
    current_word = []

    for char in input_string:
        if char == ' ' and not in_quote:
            if current_word:
                words.append(''.join(current_word))
                current_word = []
        elif char == '"':
            if in_quote:
                in_quote = False
                if current_word:
                    words.append(''.join(current_word))
                    current_word = []
            else:
                in_quote = True
        else:
            current_word.append(char)

    if current_word:
        words.append(''.join(current_word))

    return words


def extract_and_format(string):
    """
    Extracts and formats values from a string containing double-quoted strings
    and integers.

    Parameters:
        string (str): The input string to extract values from.

    Returns:
        list of str: A list containing extracted values as strings,
        preserving double-quoted strings and converting integers to strings.
    """
    args = re.findall(r'"([^"]*?)"|(\d+)', string)
    args = [str(val) if val else str(num) for val, num in args]
    return args


class HBNBCommand(cmd.Cmd):
    """
    A command-line interpreter for interacting with HBNB data.

    Attributes:
    - prompt (str): The command prompt for the interpreter.
    - __classes (set): A set containing the names of supported HBNB classes.
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            }

    def do_create(self, arg):
        """Usage: create <class_name>
        Create a new class instance and print it's id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Usage: show <class_name> <id>
        Display the string representation of an instance based on the class
        name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in obj_dict:
                print(obj_dict[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Usage: destroy <class_name> <id>
        Deletes an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in obj_dict:
                del obj_dict[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all <class_name>
        Display all instances or all instances of a specified class."""
        args = arg.split()
        obj_dict = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in obj_dict.values()])
        elif args[0] in self.__classes:
            matching_objects = []
            for key, obj in obj_dict.items():
                if key.split('.')[0] == args[0]:
                    matching_objects.append(str(obj))
            print(matching_objects)
        else:
            print("** class doesn't exist **")

    def default(self, arg):
        """Handle custom commands based on class name"""
        command_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count
                }
        args = arg.split('.')

        if len(args) > 1 and args[0] in self.__classes:
            class_name = args[0]
            command = args[1].split('(')
            if command[0] in command_dict.keys():
                command_args = " ".join(extract_and_format(command[1]))
                full_command_args = f"{class_name} {command_args}"
                return command_dict[command[0]](full_command_args)
        print(f"*** Unknown syntax: {arg}")
        return False

    def do_update(self, arg):
        """Usage: update <class_name> <id> <attr_name> "<attr_value>"
        Updates an instance based on class name and id by adding or updating
        attributes"""
        args = custom_split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key not in obj_dict:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = obj_dict[key]
                obj.__dict__[args[2]] = args[3]
                obj.save()

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        args = arg.split()
        obj_dict = storage.all()
        count = 0
        for obj in obj_dict.values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def emptyline(self):
        """Override the default behavior of executing the previous command for
        an empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
