#!/usr/bin/python3
"""This module contains the Base class"""

import json
import os.path


class Base:
    """This is the base class that monitors the id"""
    __nb_objects = 0

    def __init__(self, id=None):
        """This runs when a new instance is created"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This returns the json string representation
        of the list of dictionaries passed
        """

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This writes the JSON string representation
        of object list passed into to a file
        """

        if list_objs is None:
            list_objs = []

        new = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__),
                  mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """
        This converts a JSON string representstion into
        a list of dictionary
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This returns an instance with the attributes already set"""
        if len(dictionary) == 1:
            new = cls(5)
        else:
            new = cls(5, 5)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """This method loads a json string and converts it into an instance
        """

        if not os.path.exists('{}.json'.format(cls.__name__)):
            return []
        with open("{}.json".format(cls.__name__),
                  mode="r", encoding="utf-8") as f:
            json_string = f.read()

        list_dict = cls.from_json_string(json_string)
        instances = []

        for dic in list_dict:
            instances.append(cls.create(**dic))
        return instances
