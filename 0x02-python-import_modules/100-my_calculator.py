#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if arg[2] != "+" and arg[2] != "-" and arg[2] != "*" and arg[2] != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(arg[1])
    b = int(arg[3])
    if arg[2] == "+":
        print("{} {} {} = {}".format(a, arg[2], b, calc.add(a, b)))
    elif arg[2] == "-":
        print("{} {} {} = {}".format(a, arg[2], b, calc.sub(a, b)))
    elif arg[2] == "*":
        print("{} {} {} = {}".format(a, arg[2], b, calc.mul(a, b)))
    else:
        print("{} {} {} = {}".format(a, arg[2], b, calc.div(a, b)))
