#!/usr/bin/env python3

""" File Storage Module
    Contains the FileStorage class that serializes
        and deserializes JSON representations of class instances
"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review


class FileStorage:
    """
        serialises and deseralises json files

        File Storage
        Args:
            file_path = 'file.json' : class attribute (private)
            objects = {}:             class attribute (private)

        Functions:
            all(self)
            new(self, obj)
            save(self)
            reload(self)

    """

    __file_path = 'file.json'
    __objects = {}

    class_dict = {
        "BaseModel": BaseModel, "City": City, "Place": Place, "Review": Review,
        "State": State, "User": User, "Amenity": Amenity
    }

    # There is no __init__ function necessary here
    def all(self):
        ''' Return dictionary of <class>.<id> : object instance '''
        return self.__objects

    def new(self, obj):
        ''' Create a new object element of <class>.<id> : onject instance '''
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        ''' save object information to "file.json" '''

        file_dict = {}
        for key, obj in self.__objects.items():
            file_dict[key] = obj.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(file_dict, f)

    def reload(self):
        ''' Reload objects from JSON file.
            If file.json exists, convert dicts back to instances
        '''
        try:
            with open(self.__file_path, 'r') as f:
                new_obj = json.load(f)

                for key, val in new_obj.items():
                    obj = self.class_dict[val["__class__"]](**val)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
