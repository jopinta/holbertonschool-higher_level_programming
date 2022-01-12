#!/usr/bin/python3
'''manage urllib.error.HTTPErro'''

from urllib import request
from sys import argv
from urllib import error


if __name__ == "__main__":
    try:
        with request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
