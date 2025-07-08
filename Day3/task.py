
print("Welcome to Treasure Island. Your mission is to find the treasure.")



playing = True

while playing:

    direction_choice = input("You have hit a crossroads. Would you like to go left or right?\n")
    
    if (direction_choice.lower() == "left"):
        
        swim_decision = input("You have reached a large river. Would you like to swim or wait?\n")

        if (swim_decision.lower() == "wait"):

            door_decision = input("You have come upon three different colored doors: Red, Yellow and Blue. Which door would you like to enter?\n")

            if (door_decision.lower() == "red"):
                print("Burned by fire. Game Over.")

                play_again = input("Would you like to play again? (y or n)\n")

                if (play_again == "y"):
                    continue
                else:
                    playing = False
                    break
            elif(door_decision.lower() == "blue"):
                print("Eaten by beasts. Game Over.")

                play_again = input("Would you like to play again? (y or n)\n")

                if (play_again == "y"):
                    continue
                else:
                    playing = False
                    break
            elif(door_decision.lower() == "yellow"):
                print("You Win!.")

                play_again = input("Would you like to play again? (y or n)\n")

                if (play_again == "y"):
                    continue
                else:
                    playing = False
                    break
            else:
                print("Game Over.")

                play_again = input("Would you like to play again? (y or n)\n")

                if (play_again == "y"):
                    continue
                else:
                    playing = False
                    break
        else:
            print("Attacked by trout. Game Over")

            play_again = input("Would you like to play again? (y or n)\n")

            if (play_again == "y"):
                continue
            else:
                playing = False
                break
    else:
        print("Fall into a hole. Game Over")
        
        play_again = input("Would you like to play again? (y or n)\n")

        if (play_again != "y"):
            playing = False
            break