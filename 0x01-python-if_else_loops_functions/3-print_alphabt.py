#!/usr/bin/python3
for c in range(97, 123):
    if chr(c) != "q" and chr(c) != "e":
        print("{:s}".format(chr(c)), end="")
