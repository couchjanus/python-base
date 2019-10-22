#! /usr/bin/env python
# coding: utf

print('{}{}'.format("Super Calc".title().center(40, '='), '\n'))

print("_"*40)

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
    print('{!s}{}'.format("| Select operation:".title()+" "*20+'|', '\n'))
    print('{}'.format("|"+" "*10 + "+ : add".swapcase().rjust(15, ' ')))
    print('{}'.format("| - : Subtract".capitalize().rjust(30, ' ')))
    print('{}'.format("| * : Multiply".lower().rjust(30, ' ')))
    print('{}'.format("| / : Divide".title().rjust(28, ' ')))
    print('{}'.format("| //: Int Divide".upper().rjust(32, ' ')))
    print('{}'.format("| % : Modulo Divide".capitalize().swapcase().rjust(35, ' ')))
    print('|'+"_"*38+'|')
    return input('{!r:~^40}'.format("Enter choice(+|-|*|/|//|%):"))

while True:
    # Store the user input an operator
    operator = menu()

    if operator == 'q':
        # print('{!r}'.format('Thank You for using calculator.py!'))
        print('{!s}'.format('Thank You for using calculator.py!'))
        break # это останавливает цикл while
    
    # Convert strings into floats
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    if operator == "+":
        print ("{:+08.2f} + {:+08.2f} = {:+08.2f}".format(a, b, add(a, b)))
    elif operator == '-':
        print ("{:+08.2f} - {:+08.2f} = {:+08.2f}".format(a, b, subtract(a, b)))
    elif operator == "*":
        print ("{0} * {k} = {1}".format(a, multiply(a, b), k=b))
    # elif operator == '*':
    #     print ("{:+08.2f} * {:+08.2f} = {:+08.2f}".format(a, b, multiply(a, b)))
    # Краткая запись мат. операций и присваивания
    elif (operator == "/" or operator == "//" or operator == "%" ) and b==0:
        print("Oops, division or modulo by zero")
    elif operator == "//" and b !=0:
        print("a // b = ", idivide(a, b))
    elif operator == "%" and b !=0:
        print("a % b = ", modulo(a, b))
    elif operator == "/" and b !=0:
        print("{} {:+08.2f}".format("a / b = ", divide(a, b)))

    # If none of the above conditions were true then execute this by default
    else:
        print("Use either + - * / or % next time")
