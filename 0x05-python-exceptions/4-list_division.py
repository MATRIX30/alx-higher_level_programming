#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    i = 0
    res = 0
    while (i < list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            res_list.append(res)
            res = 0
        i = i + 1
    return res_list
