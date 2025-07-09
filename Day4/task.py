import random

scissors = "    ____\n---' ____)_____\n         ______)\n      __________)\n     (____)\n--.__(____)"
paper = "    ______\n---'  ____)____\n        _______)\n         _______)\n       ________)\n--.__________)"
rock = "    ______\n---'  ____)\n      (____)\n      (____)\n      (____)\n--._______)"

print("welcome to Rock, Paper, Scissors.")

choices = ["Rock", "Paper", "Scissors"]
choices_hand = dict(rock = rock, paper = paper, scissors = scissors)

playing = True

while playing:

    bot_choice = random.choice(choices)

    player_choice = input("Would you like to choose Rock, Paper or Scissors?\n").title()

    print(f"The bot chose: {bot_choice}.")
    print(choices_hand.get(bot_choice.lower()))
    playing = False

    print(f"You chose {player_choice}.")
    print(choices_hand.get(player_choice.lower()))

    if player_choice == "Rock" and bot_choice == "Scissors":
        print("You Win!")
    elif player_choice == "Paper" and bot_choice == "Rock":
        print("You Win!")
    elif player_choice == "Scissors" and bot_choice == "Paper":
        print("You Win!")
    elif player_choice == bot_choice:
        print("It's a tie. Try Again!")

        continue
    
    play_again = input("Would you like to play again? (y or n)\n")

    if play_again != "y":
        playing = False