# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo


print(logo)

def blind_auction():
    auction_dict = {}

    while True:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        auction_dict[name] = bid

        add_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

        if add_bid == 'yes':
            print("\n" * 20)
            continue
        elif add_bid == 'no':
            break

    winner = max(auction_dict, key=auction_dict.get)
    print(f"The winner is {winner} with a bid of ${auction_dict[winner]}!")

blind_auction()
