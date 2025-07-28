
#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        sous_list = my_list[:x]
        nb_prints = 0
        for i in sous_list:
            print(i, end='')
            nb_prints += 1
        print()
        return nb_prints
    except IndexError:
        for i in my_list:
            print(i, end='')
            nb_prints += 1
        print()
        return nb_prints
