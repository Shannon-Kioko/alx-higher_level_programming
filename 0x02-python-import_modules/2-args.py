#!/usr/bin/python3
import sys


if __name__ == "__main__":
    arguments = sys.argv[1:]
    numo_arguments = len(arguments)

    if numo_arguments == 0:
        print("0 arguments.")
    else:
        print(
            "{} argument{}:".format(
                numo_arguments, "s" if numo_arguments != 1 else ""
            )
        )
        for i, arg in enumerate(arguments, start=1):
            print("{}: {}".format(i, arg))