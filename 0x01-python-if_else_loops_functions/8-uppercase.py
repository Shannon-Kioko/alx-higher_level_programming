#!/usr/bin/python3
def uppercase(str):
    output = ""
    for c in str:
        if "a" <= c <= "z":
            uppercase_char = chr(ord(c) - 32)
            output += "{:s}".format(uppercase_char)
        else:
            output += "{:s}".format(c)
    output += "\n"
    print(output, end="")
