def search_replace(my_list, search, replace):
    new_l = my_list.copy()
    for i in range (len(new_l)):
        if new_l[i] == search:
            new_l[i]=replace
    return new_l

my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(new_list)
print(my_list)
