#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    sum = 0
    if (arg_count == 1):
        print(sum)
    else:
        i = 1
        while (i < arg_count):
            sum += int(sys.argv[i])
            i += 1
        print(sum)
