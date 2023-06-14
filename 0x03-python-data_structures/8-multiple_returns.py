#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        my_tuple = (0, None)
        return (my_tuple)
    my_tuple = (len(sentence), sentence[0])
    return (my_tuple)
