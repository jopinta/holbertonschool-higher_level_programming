#!/usr/bin/python3
'''displays the value of var found in the header of the response.'''

from urllib import request
from sys import argv
if __name__ == '__main__':
    with request.urlopen(argv[1]) as quest:
        print(quest.headers.get('X-Request-Id'))
