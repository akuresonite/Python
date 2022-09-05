import random

print("Welcome to the Rock, Paper, Scissors")
r = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while True:
    yourChoice = input("What do you choose? R, P, or S ").lower()
    choices = [r, p, s]
    player = ''
    pc = random.choice(choices)
    if yourChoice == 'r':
        player = r
    elif yourChoice == 'p':
        player = p
    elif yourChoice == 's':
        player = s
    else:
        print("Invalid Input!")
        exit()
    print(f"You choose; {player}\nComputer choose; {pc}")

    #  (rock - scissors), (papers - rock), (scissors - paper)
    if player == r and pc == s:
        print("You Win")
    elif player == p and pc == r:
        print("You Win")
    elif player == s and pc == p:
        print("You Win")
    elif player == pc:
        print("It's a draw")
    else:
        print("You Lose")
    again = input("Do you wanna try again? Y or N ").lower()
    print()
    if again == 'y':
        continue
    elif again == 'n':
        print("See you soon.")
        exit()
    else:
        print("Invalid Input!")
        exit()
