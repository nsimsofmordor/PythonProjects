# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

# Get info
name = str(input("Enter Name: "))
age = int(input("Enter Age: "))

# Print info
print(f"Hello {name}, your age is {age}")

# Get current year when age is 100
year_when_100 = (100 - age) + datetime.date.today().year

# Print results
print(f"{name}, you will turn 100 during the year of {year_when_100}")

# Needed : Input validation


