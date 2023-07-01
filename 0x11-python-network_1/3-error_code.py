#!/usr/bin/python3
"""This script takes in a URL and sends
a request to the URL and displays the body
of the response"""


import urllib.request 
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read())
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code)) 
