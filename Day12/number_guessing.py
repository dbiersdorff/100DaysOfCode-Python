import random

number = random.randint(1,101)

difficulty = input("Choose a difficulty. Type 'easy; or 'hard': ")

num_guesses = 0
if difficulty == "easy":
    num_guesses = 10
else:
    num_guesses = 5

cur_guess = num_guesses

while cur_guess > 0:
    print(f"You have {cur_guess} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"{guess} is the correct number. You won with {cur_guess} attempts remaining.")
        cur_guess = 0
    elif guess < number:
        print(f"{guess} is less than the number.")
        cur_guess -= 1
    elif guess > number:
        print(f"{guess} is greater than the number.")
        cur_guess -= 1