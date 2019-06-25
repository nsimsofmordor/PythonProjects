import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 and 20...")

# Ask the player to guess 6 times
for guessesTaken in range(1, 7):  # loops 6 times
    print("Take a guess: ")

    try:  # if the input is not a number, keep asking to take the first guess
        guess = int(input())
    except ValueError:
        print("You need to enter a number!")
        continue

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break  # this executes if the number is accurately guessed, break out of for loop

if guess == secretNumber:
    print("You got it!")
else:
    print("Nope, the number I was thinking of was " + str(secretNumber))

