#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    len(arg)
    if len(arg) == 1:
        print("0 arguments.")
    else:
        if len(arg) == 2:
            print("{} argument:".format(len(arg) - 1))
        else:
            print("{} arguments:".format(len(arg) - 1))
        for i in range(1, len(arg)):
            print("{}: {}".format(i, arg[i]))
