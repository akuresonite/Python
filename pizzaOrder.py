print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").lower()
if size!='s' or size!='m' or size!='l':
    print("Invalid Input!")
    exit()
pepp = input("Do you want pepperoni? Y or N ").lower()
if pepp!='y' or size!='n':
    print("Invalid Input!")
    exit()
cheese = input("Do you want extra cheese? Y or N ").lower()
if cheese!='y' or size!='n':
    print("Invalid Input!")
    exit()
bill = 0
if size == 's' and pepp=='y':
    bill += 17
elif size == 's' and pepp=='n':
    bill += 15
elif size == 'm' and pepp=='y':
    bill += 23
elif size == 'm' and pepp=='n':
    bill += 20
elif size == 'l' and pepp=='y':
    bill += 28
elif size == 'l' and pepp=='n':
    bill += 25
if cheese == 'y':
    bill+=1
elif cheese=='n':
    bill+=0
print(f"Your final bill is: ${bill}")