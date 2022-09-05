print("Welcome to the Love Calculator!")
while True:
    n1 = input("What is your name?\n ").lower()
    n2 = input("What is their name?\n ").lower()
    #  T R U E  L O V E
    t = n1.count('t') + n2.count('t')
    r = n1.count('r') + n2.count('r')
    u = n1.count('u') + n2.count('u')
    e = n1.count('e') + n2.count('e')
    l = n1.count('l') + n2.count('l')
    o = n1.count('o') + n2.count('o')
    v = n1.count('v') + n2.count('v')

    a = t + r + u + e
    b = l + o + v + e

    # score = (a * 10) + b
    score = int(str(a)+str(b))
    print()
    if score <= 10 or score >= 90:
        print(f"Your score is {score}, you go together like coke and mentos.")
    elif 40 <= score <= 50:
        print(f"Your score is {score}, you are alright together.")
    else:
        print(f"Your score is {score}")
    again = input("Do you wanna try again? Y or N\n ").lower()
    if again=='y':
        continue
    elif again=='n':
        break
    else:
        print("Invalid Input!")
print("See you next time!")