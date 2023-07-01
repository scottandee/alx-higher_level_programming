#!/usr/bin/python3
"""This script takes in a url and sends the passed
url with the email as a parameter and displays the
body of the response"""


from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    value = {}
    value["email"] = email

    data = parse.urlencode(value)
    data = data.encode("ascii")

    req = request.Request(url, data)
    with request.urlopen(req) as response:
        content = response.read()

    print(content.decode("utf8"))
