#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    greater = my_list[0]
    for num in my_list:
        if num > greater:
            greater = num

    return greater
