#!/usr/bin/python3
"""This script takes in a URL and display
the body of the response"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        req = requests.get(url)
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print("Error: {}".format(e.code))L
