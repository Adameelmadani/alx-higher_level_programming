#!/bin/usr/python3

"""
This is the module
"""


class LockedClass:
    """
    This is lockedClass
    """

    @staticmethod
    def raiseErr(my_name):
        """
        Raise Error
        """
        return ("'LockedClass' object has no attribute '{}'".format(my_name))

    def __setattr__(self, name, value):
        """
        setattr for dynamic
        """
        if name not in self.__dict__:
            if name != "first_name":
                raise AttributeError(LockedClass.raiseErr(name))
            super().__setattr__(name, value)
