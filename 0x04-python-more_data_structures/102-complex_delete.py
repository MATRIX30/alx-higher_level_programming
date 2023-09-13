#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_del = []
    if value in a_dictionary.values():
        for key in a_dictionary:
            if a_dictionary[key] == value:
                keys_del.append(key)
        for k in keys_del:
            a_dictionary.pop(k)
    return a_dictionary
