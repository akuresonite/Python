number = 18
guessCount = 0
guessLimit = 5
while True:
    num = int(input('Enter no.: '))
    guessCount += 1
    if num > number and guessCount < guessLimit:
        print('Guess a lesser number.')
        print('You hava left', guessLimit - guessCount, 'guesses')
        continue
    elif num < number and guessCount < guessLimit:
        print('Guess a greater number.')
        print('You hava left', guessLimit - guessCount, 'guesses')
        continue
    elif num == number and guessCount < guessLimit:
        print('Congrats, you got it in', guessCount, 'guesses')
    elif guessCount == guessLimit:
        print('Game Over')

    again = input('Do you wanna try again(y/n): ')
    if again == 'y':
        guessCount = 0
        continue
    elif again == 'n':
        print('Ok, see you next time')
        break
    else:
        print('Oops! Invalid input')
        break
