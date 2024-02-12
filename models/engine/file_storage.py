#!/usr/bin/python3
"""The implementation of the FileStorage module"""

import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """A class that defines the attributes for the FileStorage modules"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the `obj` with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objects.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f, default=str)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                data = json.load(f)
                for key, obj in data.items():
                    class_name = obj.get("__class__")
                    if class_name and class_name in globals():
                        cls = globals()[class_name]
                        self.new(cls(**obj))
        except FileNotFoundError:
            return

