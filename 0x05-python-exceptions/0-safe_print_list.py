#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        my_list[x]
        while (i < x):
            print(my_list[i], end="")
            i += 1

    except IndexError:
        i = 0
        for item in my_list:
            i += 1
            print(item, end="")
    print(end="\n")
    return (i)
