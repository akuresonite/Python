print('Welcome to the tip calculator.')
tbill = float(input('What was the total bill? $'))
p = int(input('How many people to split the bill? '))
tip = int(input('What percentage tip you like to give? 10, 12, or 15? '))
pay = str(round((tbill*(1+(tip/100)))/p, 2))
print('Each person should pay: $'+pay)