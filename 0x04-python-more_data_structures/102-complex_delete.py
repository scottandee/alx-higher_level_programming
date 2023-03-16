#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in a_dictionary.items():
        if i[1] == value:
            a_dictionary.pop(i[0])
            break
