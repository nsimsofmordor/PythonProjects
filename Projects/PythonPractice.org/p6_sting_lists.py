# Ask the user for a string and print out whether this string is a palindrome or not.

my_str = str(input("Enter a string to check if it is a palindrome or not: ").lower())

rev_str = my_str[::-1].lower()

if my_str == rev_str:
    print("Palindrome!")
else:
    print("Not Palindrome!")