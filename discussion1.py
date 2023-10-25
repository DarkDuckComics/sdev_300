"""
Program that asks the user to guess a random number.
Then will tell the user if their guess is wrong.
Hinting whether to guess higher.
Or lower until they guess right.
Prints the random number and how many tries it took.
"""
import random

# Generate a random number between 1 and 100
randomNumber = random.randint(1, 100)

# Initialize a variable to keep track of the number of attempts
ATTEMPTS = 0

while True:
    # Ask the user for a guess
    userGuess = int(input("Guess the number between 1 and 100: "))

    # Increment the number of attempts
    ATTEMPTS += 1

    # Check if the guess is correct
    if userGuess == randomNumber:
        print(f"Congratulations! You guessed the number {randomNumber} in {ATTEMPTS} attempts.")
        break
    if userGuess < randomNumber:
        print("Wrong answer. Try a higher number.")
    else:
        print("Wrong answer. Try a lower number")
