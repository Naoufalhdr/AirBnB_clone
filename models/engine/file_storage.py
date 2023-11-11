#!/usr/bin/python3
"""This module file_storage.py defines the FileStorage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    FileStorage class manages the serialization and deserialization of
    instances to and from a JSON file.

    Attributes:
    - __file_path (str): The path to the JSON file for storing serialized data
    - __objects (dict): A dictionary containing instances as values, with keys
      formatted as "<class_name>.<id>".
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of all instances."""
        return self.__objects

    def new(self, obj):
        """Adds a new instance to the dictionary."""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """Serializes and saves the dictionary of instances to the JSON file.
        """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes and reloads the dictionary of instances from the JSON
        file."""
        try:
            with open(self.__file_path) as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
