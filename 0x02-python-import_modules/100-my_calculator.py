#!/usr/bin/python3

if __name__ == "__main__":
    """ handle basic operations"""
    from calculator_1.py import add, sub, mul, div
    import sys
    count = len(sys.argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(argv[1])
    operation = int(argv[2])
    b = int(argv[3])
    if operation == '+':
        print("{} {} {} = {}".format(a, operation, b, add(a, b)))
    elif operation == '-':
        print("{} {} {} = {}".format(a, operation, b, sub(a, b)))
    elif operation == '*':
        print("{} {} {} = {}".format(a, operation, b, mul(a, b)))
    elif operation == '/':
        print("{} {} {} = {}".format(a, operation, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    
