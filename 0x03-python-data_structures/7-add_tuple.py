#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_a = list(tuple_a) 
    new_b = list(tuple_b)
    if len_a == 0:
        new_a.append(0) 
    if len_a == 1:
        new_a = [0, 0]
    if len_b == 0:
        new_b.append(0)
    if len_b == 1:
        new_b = [0, 0]
    add1 = new_a[0] + new_b[0]
    add2 = new_a[1] + new_b[1]
    add = (add1, add2)
    return add
