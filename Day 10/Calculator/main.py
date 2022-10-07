# calculator

# Add
def add(n1, n2):
    return n1 + n2


# subtract
def subtract(n1, n2):
    return n1 - n2


# multiply
def multiply(n1, n2):
    return n1 * n2


# divide
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# num1 = int(input("What's the first number?: "))
#
# for key in operations:
#     print(key)
# operation_symbol = input("Pick an operation from the line above: ")
#
# num2 = int(input("What's the second number?: "))
#
# first_answer = operations[operation_symbol](num1, num2)
# print(f"{num1} {operation_symbol} {num2} = {first_answer}")
#
# operation_symbol = input("Pick another operation: ")
# num3 = int(input("What's the next number?: "))
#
# second_answer = operations[operation_symbol](first_answer, num3)
# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
# #print(type(operations[operation_symbol]))
from art import logo


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
