#!/usr/bin/python3
"""Module that inherites from list"""


class MyList(list):
    """class MyList that inherits from list

    Args:
            list (list): list type
    """

    def print_sorted(self):
        """function to print sorted list

        Args:
                my_list (list): list to be printed in sorted order
        """
        print(sorted(self))
