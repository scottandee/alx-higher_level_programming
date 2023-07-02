#!/usr/bin/python3
"""This script sends a post request to a url
with an email passed as a parameter"""


import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {}
    values["email"] = email

    req = requests.post(url, data=values)

    print(req.text)
