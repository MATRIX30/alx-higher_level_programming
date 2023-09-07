#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)
    if arg_count == 2:
        print("1 argument:")
        print(f"1: {sys.argv[1]}")
    elif arg_count == 1:
        print("0 arguments.")
    else:
        print(f"{arg_count - 1} arguments:")
        i = 1
        while (i < arg_count):
            print(f"{i}: {sys.argv[i]}")
            i += 1
