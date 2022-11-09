import random

rand_number = random.randint(1, 100)
user_number = ""

while user_number != rand_number:
    user_number = int(input("Guess the number: "))
    if user_number > rand_number:
        print("Too high")
    if user_number < rand_number:
        print("Too low")
print(f" The correct number is: {rand_number}. Well done")
