'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
'''

a = [5, 10, 23, 60, 201]

def list_ends(a_list):
    "returns the first and last element in a list"
    return [a[0], a[-1]]

print(list_ends(a))