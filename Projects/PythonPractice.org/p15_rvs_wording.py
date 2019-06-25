# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

a = "One, Two, Three"




def reverse_string(a_string):
    return " ".join(a_string.split()[::-1])


print(reverse_string(a))