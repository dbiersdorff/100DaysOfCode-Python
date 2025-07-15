import random
import game_data

def get_option(game_options):
    return random.choice(game_options)

def check_guess(option_a, option_b, guess):
    a_followers = option_a["follower_count"]
    b_followers = option_b["follower_count"]
    if guess == "a":
        if a_followers > b_followers:
            return True
        else:
            return False
    else:
        if a_followers < b_followers:
            return True
        else:
            return False

def to_string_a(option):
    return f"Compare A: {option['name']} a {option['description']}, from {option['country']}"

def to_string_b(option):
    return f"Against B: {option['name']} a {option['description']}, from {option['country']}"


# a = get_option(game_data.data)
# b = get_option(game_data.data)
# print(f"A: {a}")
# print(f"B: {b}")
# print(check_guess(a, b, "higher"))

def game():
    win_count = 0
    check = True
    option_a = get_option(game_data.data)

    while check:
        option_b = get_option(game_data.data)

        print(to_string_a(option_a))
        
        print(to_string_b(option_b))

        guess = input("Who has more followers? ")

        check = check_guess(option_a, option_b, guess.lower())

        if check == True:
            win_count += 1
            print(f"You're right! {option_b["name"]} has {option_b["follower_count"]} million followers. Current Score: {win_count}.")
            option_a = option_b
        else:
            print(f"WRONG! {option_a["name"]} has {option_a["follower_count"]} million followers. {option_b["name"]} has {option_b["follower_count"]} million followers.")
            print(f"Final score: {win_count}.")
            

game()