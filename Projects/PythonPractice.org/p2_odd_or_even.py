# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.

# Ask for a positive number

number = int(input("Enter a positive number: "))

while number < 0:
    number = int(input("Enter a positive number: "))

# print out if odd or even
if number % 4 == 0:
    print("Multiple of 4")
elif number % 2 == 0:
    print("Even")
else:
    print("Odd")
