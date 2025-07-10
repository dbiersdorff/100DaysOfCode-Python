
import random

zero = '''
 _______
 |     |
       |
       |
       |
 ______|
'''

one = '''
 _______
 |     |
 o     |
       |
       |
 ______|
'''

two = '''
 _______
 |     |
 o     |
 |     |
       |
 ______|
'''


three = '''
 _______
 |     |
 o     |
 |     |
 /     |
 ______|
'''

four = '''
 _______
 |     |
 o     |
 |     |
 /\\    |
 ______|
'''

five = '''
 _______
 |     |
 o     |
\\|     |
 /\\    |
 ______|
'''

six = '''
    _______
    |     |
    o     |
    \\|/   |
    /\\    |
    ______|
    '''

hanging = [zero, one, two, three, four, five, six]
words = ["Banana", "Ice Cream", "Pizza"]
num_wrong = 0

def check_letter(letter, word):

    word_list = list(word)

    pos = []
    cur = 0
    for char in word_list:
        if char == letter:
            pos.append(cur)
        cur += 1
    
    return pos

def add_letter(letter, cur_guess, word):

    word_list = list(word)
    cur_guess_list = list(cur_guess)

    for i in range(0, len(word_list)):
        if word_list[i] == letter:
            cur_guess_list[i] = letter

    return ''.join(cur_guess_list)

def check_win(word):

    word_list = list(word)

    if "_" in word_list:
        return False
    else:
        return True

word = random.choice(words).lower()
cur_guess = "_"*len(word)
cur = 0
num_wrong = 0
playing = True
guesses = set()

while playing:

    guess = input("Guess a letter in this word.")

    positions = check_letter(guess, word)
    print(len(positions))
    if len(positions) > 0:
        print(hanging[num_wrong])
        cur_guess = add_letter(guess, cur_guess, word)
    else:
        guesses.add(guess)
        num_wrong += 1
        print(hanging[num_wrong])
        print(f"Letter Not in the Word. Here are your guesses:\n {guesses}")

    print(cur_guess)

    if check_win(cur_guess):
        print("Congrats you won!")
        playing = False
    elif num_wrong > 5:
        print("You Lose.")
        playing = False
