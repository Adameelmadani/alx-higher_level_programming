#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg = sys.argv
    l = len(arg)
    if l == 1:
        print("0 arguments.")
    else:
        if l == 2: 
            print("{} argument:".format(l - 1))
        else:
            print("{} arguments:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, arg[i]))
