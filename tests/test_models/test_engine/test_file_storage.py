#!/usr/bin/python3
"""The implementation of the FileStorage module"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """A class that defines the attributes and methods for the FileStorage module."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects.

        Returns:
        dict: A dictionary containing all stored objects.
        """
        return self.__objects

    def new(self, obj):
        """Add the given object to __objects with key <obj class name>.id.

        Parameters:
        self (FileStorage): The instance of the FileStorage class.
        obj: The object to be added to __objects.
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file.

        Parameters:
        self (FileStorage): The instance of the FileStorage class.
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """Deserialize the JSON file to __objects.

        Parameters:
        self (FileStorage): The instance of the FileStorage class.

        Returns:
        None
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

