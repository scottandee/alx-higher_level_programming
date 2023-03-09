#!/usr/bin/python3
if __name__ == '__main__':
# import builtin for argv
    import sys
# store length in a variable
    length = len(sys.argv)
# check if it has any arguments apart from the one at index 0
    if length == 1:
        print("0 arguments.")
# check if it has one argument
    elif length == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
# This will now run if it has more than one argument
    else:
        print("{} arguments:".format(length - 1))
        for i in range(1, length):
            print("{}: {}".format(i, sys.argv[i]))
