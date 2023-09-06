#!/usr/bin/python3
p = 122
while (p >= 97):
    flag = 0
    if p % 2 != 0:
        p = p - 32
        flag = 1
    print("{:s}".format(chr(p)), end="")
    if flag == 1:
        p = p + 32
    p = p - 1
