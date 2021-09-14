#!/usr/bin/python3


if __name__ == "__main__":
    import sys
    argvec = len(sys.argv)
    if argvec == 1:
        print("0 arguments.")
        exit()
    elif argvec == 2:
        print("1 argument:")
        print("{}: {}".format(1, sys.argv[1]))
        exit()
    print("{:d} arguments:".format(argvec - 1))
    for i in range(1, argvec):
        print("{:d}: {}".format(i, sys.argv[i]))
