#!/usr/bin/python3


if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    add = 0
    for j in range(1, argc):
        add += int(sys.argv[j])
    print(add)
