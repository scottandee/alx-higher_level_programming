#!/usr/bin/python3
"""
This module contains a function that turns an object to JSON
"""


import json


def to_json_string(my_obj):
    """This function converts object to JSON"""

    return json.dumps(my_obj)
