#!/usr/bin/python3
'''displays the value of var found in the header of the response.'''
import urllib.parse
import urllib.request
import sys

if __name__ == '__main__':

    mail = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1]) as quest:
        print(quest.read().decode('utf-8'))
