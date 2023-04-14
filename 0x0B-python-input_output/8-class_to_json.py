#!/usr/bin/python3
"""
This module contains a function that
converts a class into JSON
"""


import json


def class_to_json(obj):
    """
    This function converts a class to JSON
    """

    d = json.dumps(obj.__dict__)
    return json.loads(d)
