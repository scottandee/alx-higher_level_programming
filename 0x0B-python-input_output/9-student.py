#!/usr/bin/python3
"""
This module contains a class called Students
its attributes
"""


class Student:
    """This is a class student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """This runs immediately after a new intance is created"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This retreives a dictionary representation of class student"""
        return self.__dict__
