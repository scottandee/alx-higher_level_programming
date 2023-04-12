#!/usr/bin/python3
"""
This module contains a function that writes JSON into a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This function converts json into an
    object and saves it into a file
    """

    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
