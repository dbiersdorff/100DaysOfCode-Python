import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# total_len = num_letters + num_numbers + num_symbols
# password = ""

# cur_selection = 0

# for char in range(1, num_letters + 1):
#     password += random.choice(letters)

# for sym in range(1, num_symbols + 1):
#     password += random.choice(symbols)

# for num in range(1, num_numbers + 1):
#     password += random.choice(numbers)

total_len = num_letters + num_numbers + num_symbols

password = []
while len(password) < total_len:

    for char in range(1, num_letters + 1):
        password += random.choice(letters)

    for sym in range(1, num_symbols + 1):
        password += random.choice(symbols)

    for num in range(1, num_numbers + 1):
        password += random.choice(numbers)

random.shuffle(password)

password_str = ""

for i in password:
    password_str += i

print(f"Your password is: {password_str}")