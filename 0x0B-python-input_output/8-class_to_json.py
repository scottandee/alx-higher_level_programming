#!/usr/bin/python3
"""
This module contains a function that
converts a class into JSON
"""


def class_to_json(obj):
    """
    This function converts a class to JSON
    """

    return obj.__dict__
