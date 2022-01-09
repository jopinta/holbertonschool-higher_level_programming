#!/usr/bin/python3
'''script that fetches an url'''

import requests

if __name__ == "__main__":
    resp = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
