'''Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.'''


def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1


while True:  # while loop so it can keep catching the error
    try:
        num = int(input("Enter a number: "))  # try this
    except ValueError:
        print("Input needs to be a number")  # if not a number, keep asking and keep looping
        continue
    else:
        break  # if all good, break from loop

while num != 1:
    num = collatz(num)
