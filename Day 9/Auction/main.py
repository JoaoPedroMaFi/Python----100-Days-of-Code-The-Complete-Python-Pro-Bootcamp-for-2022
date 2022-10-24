from art import logo

# HINT: You can call clear() to clear the output in the console

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    high_value = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > high_value:
            high_value = bidding_record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ${high_value}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        import os

        os.system('cls||clear')
