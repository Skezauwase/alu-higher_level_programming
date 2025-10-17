#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print("{}".format(chr(ord(c) - 32)) if 'a' <= c <= 'z' else "{}".format(c), end="")
    print()
