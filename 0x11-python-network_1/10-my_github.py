#!/usr/bin/python3
''' displays the body of the response.'''

from requests import get
import sys
if __name__ == "__main__":
    quest = get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
    try:
        print(quest.json().get('id'))
    except:
        pass
