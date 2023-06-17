#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    if len(roman_string) == 0:
        return (0)
    s = 0
    my_list = []
    for i in range(len(roman_string)):
        if roman_string[i] == "I":
            my_list.append(1)
        elif roman_string[i] == "V":
            my_list.append(5)
        elif roman_string[i] == "X":
            my_list.append(10)
        elif roman_string[i] == "L":
            my_list.append(50)
        elif roman_string[i] == "C":
            my_list.append(100)
        elif roman_string[i] == "D":
            my_list.append(500)
        elif roman_string[i] == "M":
            my_list.append(1000)
        else:
            return (0)
    for j in range(len(roman_string)):
        if j == (len(roman_string) - 1):
            s = s + my_list[j]
            continue
        if my_list[j] < my_list[j + 1]:
            s = s - my_list[j]
        else:
            s = s + my_list[j]
    return (s)
