#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {j: i * 2 for j, i in a_dictionary.items()}
    return new_dict
