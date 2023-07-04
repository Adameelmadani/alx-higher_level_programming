#!/usr/bin/python3

"""
This is our module
"""

import sys
"""
This is sys module
"""

arguments = sys.argv
if len(arguments) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
numbers = "0123456789"
for i in arguments[1]:
    if not i in numbers:
        if not (i == arguments[1][0] and i == "-"):
            print("N must be a number")
        sys.exit(1)
n = int(arguments[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

print(n)
