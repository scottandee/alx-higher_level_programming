#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    bol = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        print("Exception: {}".format(e), file=sys.stderr)
        bol = False
    return bol
