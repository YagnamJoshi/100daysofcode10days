from art import logo
print(logo)
new_bids="yes"
auction_dict = {}
while new_bids=="yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: Rs"))
    auction_dict[name]=bid
    print("Are there any other bidders? Type 'yes' or 'no'.")
    new_bids=input()
    if new_bids=="yes":
        print("\n"*20)
bids = []
names = []
for name in auction_dict:
    bids.append(auction_dict[name])
    names.append(name)
max_bid=max(bids)
max_bid_index = bids.index(max_bid)
max_name=names[max_bid_index]
print(f"The winner is {max_name} with a bid of Rs{max_bid}")