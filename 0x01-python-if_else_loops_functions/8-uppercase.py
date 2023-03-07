#!/usr/bin/python3
def uppercase(str):
    str_up = ""
    for i in range(len(str)):
        str_up = str_up + chr(ord(str[i]) - 32)
    print(str_up)
