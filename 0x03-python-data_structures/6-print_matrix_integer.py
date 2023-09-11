#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if (matrix == [[]]):
        print("")
    else:
        for row in matrix:
            i = 0
            while i < len(row):
                if (i == len(row)-1):
                    print("{:d}".format(row[i]), end="\n")
                else:
                    print("{:d}".format(row[i]), end=" ")
                i += 1
