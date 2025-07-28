#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    int_list = []
    for i in my_list:
        if type(i) == int:
            int_list.append(i)
        else:
            continue
    try:
        sous_list = int_list[:x]
        nb_prints = 0
        for i in sous_list:
            print("{:d}".format(i), end='')
            nb_prints += 1
        print()
        return nb_prints
    except IndexError:
        print("Index out of range")

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))