import random

rand_number = random.randint(1, 5)
user_number = ""

while user_number != rand_number:
    user_number = int(input("Guess the number: "))
    print("Still not right: ", user_number)
print(f"You got the right number: {rand_number} and {user_number}")
