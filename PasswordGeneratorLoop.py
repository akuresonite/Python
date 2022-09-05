import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the PyPassword Generator!")
nrLetters = int(input("How many letters would you like in you password? "))
nrSymbols = int(input("How many symbols would you like in you password? "))
nrNumbers = int(input("How many numbers would you like in you password? "))
n = int(input("Number of passwords: "))
for nop in range(0, n):
    password = ''
    passLength = nrLetters + nrSymbols + nrNumbers
    for i in range(nrLetters):
        # password += letters[random.randint(0, len(letters) - 1)]
        password += random.choice(letters)
    for i in range(nrSymbols):
        # password += symbols[random.randint(0, len(symbols) - 1)]
        password += random.choice(symbols)
    for i in range(nrNumbers):
        # password += numbers[random.randint(0, len(numbers) - 1)]
        password += random.choice(numbers)
    #  print(password, len(password), passLength)

    passList = [i for i in password]  # string to list
    #  print(passList)
    random.shuffle(passList)  # list shuffling
    #  print(passList)
    print(nop+1, end=' ')
    for i in passList:  # list printing without space
        print(i, end='')
    print(end=' ')

#  by using list append method
