from art import logo
def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add, "-": minus, "*": multiply, "/": divide
}


def calculator():
    print(logo)
    n1 = eval(input("Enter the first number: "))
    for i in operations:
        print(i)
    while True:
        operation_symbol = input("Pick an operation: ")
        n2 = eval(input("Enter the next number: "))
        calFunction = operations[operation_symbol]
        answer = calFunction(n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")
        again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or type 'e' to exit.: ")
        if again == 'y':
            n1 = answer
            continue
        elif again == 'n':
            calculator()
        elif again == 'e':
            exit()
        else:
            print("Invalid Input!")
            exit()

calculator()