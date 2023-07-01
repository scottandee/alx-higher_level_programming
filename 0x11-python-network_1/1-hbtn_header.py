#!/usr/bin/python3
"""This script sends a request to the url passed
as argument and prints the X-Request-Id varible
in the header of the response
"""


import urllib.request as request
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        header = response.headers.get("X-Request-Id")
    print(header)
