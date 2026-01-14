#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase"""
    for c in str:
        char = (chr(ord(c) - (ord('a') - ord('A')))
                if 'a' <= c <= 'z' else c)
        print("{}".format(char), end="")
    print()
    