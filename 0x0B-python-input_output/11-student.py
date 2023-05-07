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

    def to_json(self, attrs=None):
        """This retreives a dictionary representation of class student"""
        stu_dict = self.__dict__
        if attrs is None:
            return stu_dict
        mylist = []
        for i in attrs:
            if stu_dict.get(i) is None:
                continue
            mylist.append([i, stu_dict[i]])
        return dict(mylist)

    def reload_from_json(self, json):
        """This replaces all attributes of the student instance
        """
        if json == None:
            return
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
