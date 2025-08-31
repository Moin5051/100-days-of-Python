from art import logo
print(logo)


def find_highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0

    max(bidding_dict)

    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bid ={}
continue_bidding = True
while continue_bidding:
    name = input("What's your Name? : ")
    price = int(input("What's your bid? $"))
    bid[name] = price
    new = input("Is there someone else who would want to bid? 'Yes' or 'No'?").lower()
    if new == 'no':
        continue_bidding= False
        find_highest_bidder(bid)
    elif new == "yes":
        print("\n" *50)
    





