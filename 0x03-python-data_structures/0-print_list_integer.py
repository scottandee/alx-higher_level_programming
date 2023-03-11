#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Function that prints out the content of a list"""
    for i in range(len(my_list)):
        print("{}".format(int(my_list[i])))
