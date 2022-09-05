while True:
    year = int(input('Which year do you want to check? '))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year.')
            else:
                print(f'{year} is a not a leap year.')
        else:
            print(f'{year} is a leap year.')
    else:
        print(f'{year} is a not a leap year.')

    again = input('Do you want to try again? (y/n):')
    if again == 'y':
        continue
    else:
        print('See you next time.')
        break