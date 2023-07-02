#!/usr/bin/python3
"""This python script fetches a url with the
requests module"""


import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    req = requests.get(url)
    text = req.text
    print("Body response:")
    print("    - type: {}\n    - content: {}".format(type(text), text))
