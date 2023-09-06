#!/usr/bin/python3
for i in range(122, 64, -1):
    print(f"{chr(i).upper() if i % 2 == 0 else chr(i).lower()}", end="")
