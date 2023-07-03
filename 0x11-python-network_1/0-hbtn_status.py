#!/usr/bin/python3
'''This script fetches a url'''


import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    result = ''

    with urllib.request.urlopen(url) as response:
        result = response.read()

    utf8 = result.decode("UTF-8")
    print("Body response:")
    print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
          type(result), result, utf8))
