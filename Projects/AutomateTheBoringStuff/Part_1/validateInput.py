while True:
    print("Enter your age: ")
    age = input()
    if age.isdecimal():  # if age is only a decimal
        break  # break out of the while loop
    print("Your age must be a number")

while True:
    print("Select a new password (letters and numbers)")
    password = input()
    if password.isalnum():  # if pass only have nums and letters
        break  # break out of the while loop
    print("Passwords can only contain numbers a letters")

