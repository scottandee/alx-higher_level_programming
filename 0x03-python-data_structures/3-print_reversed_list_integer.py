#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints list in reverse order"""
    reverse = my_list[:]
    reverse.reverse()
    for i in range(len(reverse)):
        print("{}".format(reverse[i]))
