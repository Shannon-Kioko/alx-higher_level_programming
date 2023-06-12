#!/usr/bin/python3
def element_at(my_list, idx):
    indices = len(my_list) - 1

    if idx > indices:
        return None

    if idx < 0:
        return None

    return my_list[idx]
