#!/usr/bin/python3

"""Command line console for the AirBnb clone"""

import cmd
import json
import os
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"BaseModel": BaseModel, "User": User,
           "State": State, "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class HBNBCommand(cmd.Cmd):
    """The commandline console"""

    prompt: str = '(hbnb) '
    fetched_objects = storage.all()
    all_classnames = []
    all_ids = []
    for key in fetched_objects.keys():
        classname, class_id = key.split('.')
        all_classnames.append(classname)

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def emptyline(self):
        """An empty line should not execute anything"""
        pass

    def do_create(self, arg):
        """Creates a new instance of the BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        new_inst = classes[args[0]]()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, arg):
        """
        prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance and saves the changes  into the JSON file"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")
            return

    def do_all(self, arg):
        """prints string representation of all instances"""
        if arg and arg not in classes:
            print("** class doesn't exist **")
            return

        objects = storage.all()
        if arg:
            objs = [str(v) for k, v in objects.items()
                    if k.startswith(arg + ".")]
        else:
            objs = [str(v) for v in objects.values()]

        print(objs)


    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = f"{args[0]}.{args[1]}"
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        setattr(obj, args[2], args[3])
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
