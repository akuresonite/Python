w = eval(input('Enter your weight in kg: '))
h = eval(input('Enter your height in m: '))
bmi = round(w / (h ** 2))
print(f'your bmi is {bmi},')
if bmi < 18.5:
    print('yoy are underweight.')
elif bmi < 25:
    print('you have normal weight.')
elif bmi < 30:
    print('you are slightly overweight.')
elif bmi < 35:
    print('you are obese.')
else:
    print('you are clinically obese.')
