#! /usr/bin/env python
# coding: utf

print("Super Calc")

# Program make a simple calculator that can add, subtract, multiply and divide using functions

# define functions
def add(x, y):
    """This function adds two numbers"""

    return x + y

def subtract(x, y):
    """This function subtracts two numbers"""

    return x - y

def multiply(x, y):
    """This function multiplies two numbers"""

    return x * y

def divide(x, y):
    """This function divides two numbers"""

    return x / y

def menu():
    print("Select operation.")
    print("+.Add")
    print("-.Subtract")
    print("*.Multiply")
    print("/.Divide")
    return input("Enter choice(+|-|*|/):")

while True:
    # Store the user input an operator
    operator = menu()

    if operator == 'q':
        print('Thankyou for using calculator.py!')
        break # это останавливает цикл while
    
    # Convert strings into integers
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    if operator == "+":
        print("a + b = ", add(a, b))
    elif operator == '-':
        print("a - b = ", subtract(a, b))
    elif operator == '*':
        print("a * b = ", multiply(a, b))
    elif operator == '/':
        if b != 0:
            print("a / b = ", divide(a, b))
        else:
            print("Oops, division by zero")
    # If none of the above conditions were true then execute this by default
    else:
        print("Use either + - * / or % next time")
