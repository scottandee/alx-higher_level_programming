#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints list in reverse order"""
    copy = my_list[:]
    copy.reverse()
    for i in copy:
        print("{:d}".format(i))
