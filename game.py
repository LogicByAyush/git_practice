import random

num = random.randint(1, 100)
number = num
attempts = 1

print("I have selected a number between 1 and 100.")

while True:
    guess = int(input(f"Attempt {attempts} Please enter your guess number: "))
    attempts += 1

    if guess < number:
        print("Less guess")
    elif guess > number:
        print("Higher guess")
    else:
        print("Correct!")
        print(f"You guessed the number in {attempts-1} attempts.")
        break