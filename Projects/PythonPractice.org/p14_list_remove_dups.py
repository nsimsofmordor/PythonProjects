'''
Write a program (function!)
that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.

Extras:

    Write two different functions to do this - one using a loop and constructing a list, and another using sets.
'''

import random

a = [1, 2, 2, 3, 4, 5, 6, 7, 7]


def rm_dups(a_list):
    x = []
    for i in a_list:
        if i not in x:
            x.append(i)
    return x


def conv_set(a_list):
    a_set = set(a_list)
    return a_set


print(a)
print(rm_dups(a))
print(conv_set(a))
