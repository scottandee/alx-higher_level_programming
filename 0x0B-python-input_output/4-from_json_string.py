#!/usr/bin/python3
"""
This module contains a function that converts JSON into object
"""


import json


def from_json_string(my_str):
    """This function converts json to object"""

    return json.loads(my_str)
