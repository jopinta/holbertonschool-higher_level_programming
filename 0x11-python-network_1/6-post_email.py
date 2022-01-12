#!/usr/bin/python3
''' displays the body of the response.'''

import requests
import sys
if __name__ == "__main__":
    quest = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(quest.text)
