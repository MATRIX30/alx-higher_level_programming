#!/usr/bin/python3
for i in range(122, 64, -1):
    if i % 2 == 0:
        print(chr(i).upper(), end="")
    else:
        print(chr(i).lower(), end="")
