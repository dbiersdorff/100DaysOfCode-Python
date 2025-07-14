import random
cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}
suits = ["Diamonds", "Hearts", "Spades", "Clubs"]

def get_deck():
    deck = []
    for i in range(0, 4):

        for x in values.values():
            deck.append(x)
    
    return deck

def check_hand(hand):
    total = 0
    for x in hand:
        total += x

def check_total(hand):
    total = 0

    for x in hand:
        total += x
    
    return total

def final_dealer_hand(dealer_cards, deck):
    total = check_total(dealer_cards)
    while total < 17:
        card = deck.pop()
        dealer_cards.append(card)
        total += card

    return dealer_cards

deck = get_deck()
random.shuffle(deck)
print(deck)

playing = True

while playing:

    playing_answer = input("Would you like to play a game of Blackjack? Type 'y' or 'n': ")

    if playing_answer == "y":

        player_cards = []
        dealer_cards = []
        card_one = deck.pop()
        dealer_card = deck.pop()
        dealer_cards.append(dealer_card)
        card_two = deck.pop()
        player_cards.append(card_one)
        player_cards.append(card_two)
        print(f"Your cards: {player_cards}")
        print(f"Dealer's first card: {dealer_card}")

        hitting = True
        total = 0
        while hitting:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            
            if another_card != "y":
                hitting = False
                break

            player_cards.append(deck.pop())
            print(f"Your cards: {player_cards}")

            total = check_total(player_cards)

            if total == 21:
                print("BlackJack! You win!")
                hitting = False
                playing = False
            elif total > 21:
                print("Bust! Dealer Wins!")
                hitting = False
                playing = False
        
        dealer_cards = final_dealer_hand(dealer_cards, deck)
        total_dealer = check_total(dealer_cards)
        print(f"Dealer's final hand: {dealer_cards}")

        if total_dealer > 21:
            print("Dealer busts. You win!")
        elif total_dealer > total:
            print(f"Dealer wins with a hand of: {dealer_cards}. Your hand lost with a hand of: {player_cards}")
        else:
            print(f"You win with a hand of: {player_cards}. dealer had a hand of: {dealer_cards}")