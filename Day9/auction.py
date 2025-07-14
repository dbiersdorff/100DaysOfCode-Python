
bid_dict = {}

bidding = True
another_bid = "yes"
while bidding:



    if another_bid == "yes":

        name = input("What is your name?\n")

        bid_amount = int(input("How much would you like to bid?\n"))

        bid_dict[name] = bid_amount
    else:
        max_person = max(bid_dict)
        print(f"{max_person} won the bid with the amount of {bid_dict[max]}")
        bidding = False

    another_bid = input("Is there another bidder?\n")


