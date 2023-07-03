#!/usr/bin/python3

"""
This module prints texts
"""


def text_indentation(text):
    """
    This is the function that prints the text
    """

    if not type(text) is str:
        raise TypeError("text must be a string")
    ponc = ['.', '?', ':']
    sub_text = []
    for i in range(len(text)):
        sub_text.append(text[i])
        if (text[i] in ponc) or (i == (len(text) - 1)):
            for j in range(len(sub_text)):
                if j == 0 and sub_text[j] == ' ':
                    continue
                if j == (len(sub_text) - 1) and sub_text[j] == ' ':
                    continue
                print(sub_text[j], end="")
            if (text[i] in ponc):
                print("")
                print("")
            sub_text.clear()


if __name__ == "__main__":
    import doctest
    """
    This is doctest module
    """
    doctest.testfile("./tests/5-text_indentation")
