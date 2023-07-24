#!/usr/bin/python3
"""
7-add_item module
Contains a function that adds all arguments to a Python list,
and then save them to a file
"""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """
    Adds all arguments to a Python list, and then save them to a file
    """
    if os.path.exists("add_item.json"):
        my_list = load_from_json_file("add_item.json")
    else:
        my_list = []

    # Add command-line arguments to the list
    my_list.extend(sys.argv[1:])

    # Save the updated list to "add_item.json"
    save_to_json_file(my_list, "add_item.json")


if __name__ == "__main__":
    main()
