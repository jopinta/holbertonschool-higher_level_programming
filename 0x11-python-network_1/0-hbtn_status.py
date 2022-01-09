#!/usr/bin/python3
# script that fetches an url

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body))
    print("\t- content: {}".format(type(body))
    print("\t- utf8: {}".format(type(body.decode("utf8"))
