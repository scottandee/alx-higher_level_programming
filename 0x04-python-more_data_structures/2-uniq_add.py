#!/usr/bin/python3
def uniq_add(my_list=[]):
    first_set = set(my_list)
    add = 0
    for i in first_set:
        add = add + i
    return add
