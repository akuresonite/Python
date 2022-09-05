# from replit import clear
# HINT: You can call clear() to clear the output in the console.
bidders = {}
while True:
    print("Welcome to the secret auction program.")
    name = input(f"What is your name?: ")
    bid = int(input(f"What your bid?: $"))
    bidders[name] = bid
    again = input(f"Are there any other bidders? (y/n): ").lower()
    if again == 'y':
        # clear()
        continue
    elif again == "n":
        print(bidders)
        break
    else:
        print("Invalid Input!")
highestBid = 0
highestBidder = ''
for i in bidders:
    n = bidders[i]
    if n > highestBid:
        highestBid = n
        highestBidder = i
print(f"The winner is {highestBidder} with a bid of ${highestBid}.")

'''
Ashish
12
y
Rajesh
13
y
Sameer
11
y
Manish
67
n
'''


