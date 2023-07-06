#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
print(dict)
try:
    lc.dict = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
