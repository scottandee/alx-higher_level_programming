#!/usr/bin/python3

def weight_average(my_list=[]):
    sums = 0
    weights = 0
    if len(my_list) == 0:
        return 0
    for i in my_list:
        sums = sums + (i[0] * i[1])
        weights = weights + i[1]
    return sums / weights
