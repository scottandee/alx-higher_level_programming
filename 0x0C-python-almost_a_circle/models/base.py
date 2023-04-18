#!/usr/bin/python3
"""This module contains the Base class"""


import json


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

        for i in range(len(list_objs)):
            name = type(list_objs[i]).__name__
            list_objs[i].to_dictionary()
        with open("{}.json".format(name),
                  mode="w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        This converts a JSON string representstion into
        a list of dictionary
        """

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
