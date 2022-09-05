#  45*3=555, 56+9=77, 56/7=4
# print('Calculator')
# n1 = int(input('Enter no.: '))
# op = input('Enter operator: ')
# n2 = int(input('Enter another no.: '))
# ans = 0
#
# if (n1 == 45 or n1 == 3) and (n2 == 45 or n2 == 3) and op == '*':
#     ans = 555
# elif (n1 == 56 or n1 == 9) and (n2 == 56 or n2 == 9) and op == '+':
#     ans = 77
# elif (n1 == 56 or n1 == 7) and (n2 == 56 or n2 == 7) and op == '/':
#     ans = 4
# elif op == '+':
#     ans = n1 + n2
# elif op == '-':
#     ans = n1 - n2
# elif op == '*':
#     ans = n1 * n2
# elif op == '/':
#     ans = n1 / n2
#
# print(n1, op, n2, "=", ans)

while True:
    firstNum = input("Enter FirstNum :")
    operator = input("Enter operator :")
    secondNum = input("Enter SecondNum :")
    FaultyDict = {"45*3": "555", "56+9": "77", "56/6": "4"}
    expression = firstNum + operator + secondNum
    reverse = secondNum + operator + firstNum
    if expression in FaultyDict.keys():
        # print(FaultyDict[expression])
        print(firstNum, operator, secondNum, ' = ', FaultyDict[expression])
    elif reverse in FaultyDict.keys():
        # print(FaultyDict[reverse])
        print(secondNum, operator, firstNum, ' = ', FaultyDict[reverse])
    else:
        print(firstNum, operator, secondNum, ' = ',
              eval(firstNum + operator + secondNum))

    again = input('Do you want to contine (y/n): ')
    if again == 'y':
        continue
    elif again == 'n':
        print('OK, See you next time :)')
        break
