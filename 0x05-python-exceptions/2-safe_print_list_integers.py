#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ prints x elements  of a list and only integers

    Args:
        my_list (list, optional): can contain any type(int, str etc).
        Defaults to [].
        x (int, optional): represents number of elements to access in
        my_list Defaults to 0.
    Returns:
        the real number of integers printed
    """

    print_count = 0
    if ((x == 0) or my_list == []):
        return (print_count)
    else:
        i = 0
        try:
            while (i < x):
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    print_count += 1
                i += 1
            print(end="\n")
            return (print_count)
        except IndexError:
            pass
    
