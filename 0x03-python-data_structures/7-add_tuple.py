#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    added = []
    for i in range(2):
        if i <= len(list_b):
            list_b.append(0)
        if i <= len(list_a):
            list_a.append(0)
        added.append(list_a[i] + list_b[i])
    return tuple(added)    
