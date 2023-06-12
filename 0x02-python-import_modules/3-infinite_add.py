#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    arg = sys.argv
    for i in range(1, len(arg)):
        s = s + int(arg[i])
    print("{}".format(s))
