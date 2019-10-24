#! /usr/bin/env python
# coding: utf

title = "Super Calc" 
print(f"{title}".title().center(40, '='), '\n')

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

def calcHelp(e=''):
    print(f"\n{e}") if e != '' else print()
    print ("""
        Usage operation:
            h                        Display this usage message
            2 + 2                    Add
            3 - 1                    Subtract
            2 * 2                    Multiply
            4 / 2                    Divide
            5 // 2                   Int Divide
            7 % 3                    Nodulo Divide
            q                        Quit
        """)

def result(a, b, operator):
    """This function return result"""
    r = False
    error = ''
    if operator == "+":
        r = add(a, b)
    elif operator == '-':
        r = subtract(a, b)
    elif operator == "*":
        r = multiply(a, b)
    elif (operator == "/" or operator == "//" or operator == "%" ) and b==0:
        error = "Oops, division or modulo by zero"
    elif operator == "//" and b !=0:
        r = idivide(a, b)
    elif operator == "%" and b !=0:
        r = modulo(a, b)
    elif operator == "/" and b !=0:
        r = divide(a, b)
    else:
        error = "Use either + - * / or % next time"
    return r, error

while True:
    ops = ('+','-','*','/','//','%','**')

    choice = menu()

    if choice == 'q':
        print('{!s}'.format('Thank You for using calculator.py!'))
        break 
    
    if choice == 'h':
        calcHelp()
        continue

    for o in ops:
        index = choice.find(o)
        if index != -1:
            operator = o
            x,y = choice.split(o)
            x = x.strip()
            y = y.strip()
    
    if x.isdigit():
        a = float(x)
    else:
        calcHelp()
        continue

    if y.isdigit():
        b = float(y)
    else:
        calcHelp()
        continue

    if operator not in ops:
        calcHelp()
        continue
    
    res, err = result(a, b, operator)
    
    if err != '':
        calcHelp(err)
        continue
    else:
        print (f"{a} {operator} {b} = {res}")
