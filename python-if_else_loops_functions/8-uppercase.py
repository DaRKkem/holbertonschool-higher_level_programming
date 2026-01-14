#!/usr/bin/python3
def uppercase(str):
    """ Print a string in uppercase """
    for c in str:
        print("{}".format(chr(ord(c)-(ord('a')-ord('A')))) if 'a' <= c <= 'z' else "{}".format(c), end="")
    print()
