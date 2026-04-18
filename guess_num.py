import random
# welcoming message 
print("Welcome to the Number Guessing Game powered by")
print("Think a number from 1 - 100")

difficulty = input("Choose the Difficulty (easy) or (hard): ").lower()
# create decision
if difficulty == "easy":
    max_attempts = 10
elif difficulty == "hard":
    max_attempts = 5
else:
    print("Invalid Choice! Defficulty to easy")
    max_attempts = 10
# create a secret number
secret_number = random.randint(1, 100)
# start guessing loop
attempts = 0
while attempts < max_attempts:
    print(f"Yo have {max_attempts - attempts} attempt remaining to gues the Number")
    try:
        guess = int(input(f"Make a guess: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    attempts += 1
    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else: 
        print(f"Congratulatio! You guessed it in {attempts} attempts!")
        break
else: 
    print(f"Sorry! You've run out of attempt. The number was {secret_number}.")
#end powered by Kamal 







