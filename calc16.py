#! /usr/bin/env python
# coding: utf

print('{}{}'.format("Super Calc".title().center(40, '='), '\n'))

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
    print("_"*40)
    print('{!s}'.format("| Available operators:".title()+" "*17+'|'))
    print('{}'.format("|"+" "*10 + "+ : add".swapcase().rjust(15, ' ') +" "*13 + "|"))
    print('{}'.format("|"+" "*10 + "- : Subtract".capitalize().rjust(20, ' ') +" "*8 + "|"))
    print('{}'.format("|"+" "*10 + "* : Multiply".lower().rjust(20, ' ') +" "*8 + "|"))
    print('{}'.format("|"+" "*10 + "/ : Divide".title().rjust(18, ' ') +" "*10 + "|"))
    print('{}'.format("|"+" "*10 + "//: Int Divide".upper().rjust(22, ' ') +" "*6 + "|"))
    print('{}'.format("|"+" "*10 + "% : Modulo Divide".capitalize().swapcase().rjust(25, ' ') +" "*3 + "|"))
    print('|'+"_"*38+'|')
    return input('{}'.format("\nEnter something like 2 + 2 or q or h : "))

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
    formula = menu()
    
    fields = formula.split(" ")

    if len(fields) != 3:
        operator = fields[0]
    else:
        a = float(fields[0])
        operator = fields[1]
        b = float(fields[2])
    
    if operator == 'q':
        print('{!s}'.format('Thank You for using calculator.py!'))
        break # это останавливает цикл while
    
    if operator == 'h':
        calcHelp()
        continue

    if operator == "+":
        print ("{:+08.2f} + {:+08.2f} = {:+08.2f}".format(a, b, add(a, b)))
    elif operator == '-':
        print ("{:+08.2f} - {:+08.2f} = {:+08.2f}".format(a, b, subtract(a, b)))
    elif operator == "*":
        print ("{0} * {k} = {1}".format(a, multiply(a, b), k=b))
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
