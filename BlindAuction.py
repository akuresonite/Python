import sys
bidders = {}
c = 0
while True:
    print("Welcome to the secret auction program.")
    c += 1
    print(c, sys.argv[c])
    name = input(f"What is your name?: {sys.argv[c]}")
    c += 1
    print(c, sys.argv[c])
    bid = input(f"What your bid?: ${sys.argv[c]}")
    bidders[name] = bid
    c += 1
    print(c, sys.argv[c])
    again = input(f"Are there any other bidders? (y/n): {sys.argv[c]}").lower()
    print(f"again{again}again")
    print(c, sys.argv[c],again)
    if again == 'y':
        continue
    elif again == "n":
        print(bidders)
        break
    else:
        print("Invalid Input!")
        continue

# Ashish
# 12
# y
# Rajesh
# 13
# y
# Sameer
# 11
# y
# Manish
# 67
# n