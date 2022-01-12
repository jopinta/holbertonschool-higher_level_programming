#!/usr/bin/python3
'''displays the value of the variable X-Request-Id'''

import sys
import requests

if __name__ == '__main__':
    quest = requests.get(sys.argv[1])
    print("{}".format(quest.headers.get(X-Request-Id)))
