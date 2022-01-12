#!/usr/bin/python3
'''displays the value of the variable X-Request-Id'''

inport sys
import request

if __name__ == '__main__':
    quest = request.get(sys.argv[1])
    print("{}".format(quest.headers.get(X-Request-Id))
