#!/usr/bin/python3
"""
This module contains a function that
converts a class into JSON
"""


import json
from json import JSONEncoder


class MyEncoder(JSONEncoder):

    def default(self, obj):
        return obj.__dict__

def class_to_json(obj):
    """
    This function converts a class to JSON
    """

    d = json.dumps(obj, cls=MyEncoder)
    return json.loads(d)
