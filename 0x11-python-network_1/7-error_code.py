#!/usr/bin/python3
''' displays the body of the response.'''

import requests
import sys
if __name__ == "__main__":
    quest = requests.get(sys.argv[1])
    if quest.status_code < 400:
        print(quest.text)
    else:
        print("Error code: {}".format(quest.status_code)
