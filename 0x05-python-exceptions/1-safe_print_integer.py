#!/usr/bin/python3
def safe_print_integer(value):
    bol = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        bol = False
    return bol
