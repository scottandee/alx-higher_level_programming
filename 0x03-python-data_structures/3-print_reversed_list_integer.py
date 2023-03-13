#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints list in reverse order"""
    if my_list == None:
        return None
    for i in reversed(my_list):
        print("{:d}".format(i))
