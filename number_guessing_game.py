import random

random_number= random.randint(1, 100)
user = -1
guesses = 0

while user != random_number:
    user = int(input("Enter a number between 1 to 100: "))
    guesses += 1

    if user > random_number:
        print("Enter a lower number")
    else :
        print("Enter a higher number")

print(f"You have guessed the correct number in {guesses} attempts")