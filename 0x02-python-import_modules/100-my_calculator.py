#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)

    if arg_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
    if (sys.argv[2] not in "+-/*"):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        print("eke")
        if (sys.argv[2] == "+"):
            result = add(a, b)
        elif (sys.argv[2] == "-"):
            result = sub(a, b)
        elif (sys.argv[2] == "*"):
            result = mul(a, b)
        elif (sys.argv[2] == "/"):
            result = div(a, b)

        a = int(sys.argv[1])
        b = int(sys.argv[3])
        print(f"{a:d} {sys.argv[2]} {b:d} = {result:d}")
