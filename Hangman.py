import random

words = ['Ashish', 'Kumar', 'Uchadiya', 'Sameer', 'Nandmehar', 'Rajesh']
selected = random.choice(words)
instanceWord = []
for i in range(0, len(selected)):
    instanceWord.append('_')
# print(instanceWord)
for i in range(0, len(selected)):
    for i in range(0, len(selected)):
        print('_', end='')
    print()
    print(selected)
    print()
    letter = input("Guess letters: ")
    if letter in selected.lower():
        print(f"{letter} is a right guess.")
    for i in range(0, len(selected)-1):
        if letter == selected[i]:
            instanceWord[i] = letter
        else:
            instanceWord[i] = '_'
            continue
    print(instanceWord)
    print(instanceWord)
