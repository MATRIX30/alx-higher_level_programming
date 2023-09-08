#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    arg_count = len(argv)
    a = int(argv[1])
    b = int(argv[3])
    operation = argv[2]
    if arg_count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (argv[2] not in ["+", "-", "/", "*"]):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        if (operation == '+'):
            result = add(a, b)
        elif (operation == '-'):
            result = sub(a, b)
        elif (operation == '*'):
            result = mul(a, b)
        elif (operation == '/'):
            result = div(a, b)
        print(f"{a:d} {argv[2]} {b:d} = {result:d}")
