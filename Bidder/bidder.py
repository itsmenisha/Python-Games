# A Bidding Game
from art import logo
from replit import clear
print(logo)
dictionary = {}


def highest_bidder(bidder_record):
    highest_bid = 0
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} with a bid of {highest_bid}")


bidder_continue = True
while bidder_continue:
    a = input("Enter your name:")
    b = int(input("Enter the amount you are bidding: $"))
    c = input("Are their any more bidders: ").lower()
    dictionary[a] = b
    if c == "yes":
        bidder_continue = True
        clear()
    if c == "no":
        bidder_continue = False
        highest_bidder(dictionary)

# def bidders(name, amount):
#     new_bidder = {}
#     new_bidder["name"] = name
#     new_bidder["amount"] = amount
#     dictionary.append(new_bidder)
