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

def modulo(x, y):
    """This function divides by modulo two numbers"""

    return x % y

def idivide(x, y):
    """This function int divides two numbers"""

    return x // y

def menu():
    print("Select operation.")
    print("+.Add")
    print("-.Subtract")
    print("*.Multiply")
    print("/.Divide")
    print("//.Int Divide")
    print("%.Modulo Divide")
    return input("Enter choice(+|-|*|/|//|%):")

def calcHelp():
    print ("""
        Usage operation:
            'h'                        Display this usage message
            '+'                        Add
            '-'                        Subtract
            '*'                        Multiply
            '/'                        Divide
            '//'                       Imt Divide
            '%'                        Nodulo Divide
            'q'                        Quit
        """)
while True:
    # Store the user input an operator
    operator = menu()

    if operator == 'q':
        print('Thankyou for using calculator.py!')
        break # это останавливает цикл while
    
    if operator == 'h':
        calcHelp()
        continue
    
    # Convert strings into floats
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    if operator == "+":
        print("a + b = ", add(a, b))
    elif operator == '-':
        print("a - b = ", subtract(a, b))
    elif operator == '*':
        print("a * b = ", multiply(a, b))

    # Краткая запись мат. операций и присваивания
    elif (operator == "/" or operator == "//" or operator == "%" ) and b==0:
        print("Oops, division or modulo by zero")
    elif operator == "//" and b !=0:
        print("a // b = ", int(idivide(a, b)))
    elif operator == "%" and b !=0:
        print("a % b = ", int(modulo(a, b)))
    elif operator == "/" and b !=0:
        print("a / b = ", divide(a, b))
   
    # If none of the above conditions were true then execute this by default
    else:
        calcHelp()
