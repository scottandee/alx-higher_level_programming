#!/usr/bin/python3
"""Module containing a class that inherits from list"""


class MyList(list):
    """This is an object that inherits from a class list"""
    def print_sorted(self):
       print(sorted(self)) 
