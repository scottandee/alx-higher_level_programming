#!/usr/bin/python3
def remove_char_at(str, n):
    copy = "" + str
    if n > len(copy) or n < 0:
        return copy
    copy = copy.replace(copy[n], "")
    return copy
