#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    res = sum(my_set)
    return res

my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print(set(my_list))

print("Result: {:d}".format(result))
