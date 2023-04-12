#!/usr/bin/python3
"""This is a python module that contains function
that creates an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    This function creates an object
    from a JSON file and returns it
    """

    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
