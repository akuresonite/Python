print('Welcome to the Roller coaster!')
height = eval(input("What's your height? "))
bill = 0
if height >= 120:
    print("Wow! You can ride.")
    age = eval(input("What's your age? "))
    if 7 < age < 12:
        print("Child tickets are $5.")
        bill = 5
    elif 12 <= age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    elif 18 <= age < 45:
        print("Adult tickets are $12")
        bill = 12
    elif 45 <= age <= 55:
        print("Everything is going to be fine. Have a free ride on us.")
    elif age > 55:
        print("Adult tickets are $12")
        bill = 12
    else:
        print("! Invalid age.")
    photo = input("Do you want a photo taken?(y/n) ").lower()
    if photo == 'y':
        bill =+ 3
        print(f"The total bill is ${bill}")
    elif photo == 'n':
        print(f"The total bill is ${bill}")
    else:
        print("! Invalid input")
else:
    print("Sorry, you have to grow taller before you can ride.")
