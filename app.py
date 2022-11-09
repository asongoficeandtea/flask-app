import random


def game(number):
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {number}:  "))
        if guess > random_number:
            print("Too high")
        elif guess < random_number:
            print("Too low")
        else:
            print(f"You guessed the correct number which is {random_number}")


game(25)


""" rand_number = random.randint(1, 100)
user_number = ""

while user_number != rand_number:
    user_number = int(input("Guess the number: "))
    if user_number > rand_number:
        print("Too high")
    if user_number < rand_number:
        print("Too low")
print(f" The correct number is: {rand_number}. Well done")
"""
