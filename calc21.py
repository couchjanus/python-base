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

ops = ('+','-','*','/','//','%','**')

def menu():
    print(f"{title}".title().center(30, '='), '\n')
    print("_"*30)
    str1 = 'Select operation:'
    print('|'+str1+' '*(28-len(str1))+'|')
    print('|'+"_"*28+'|')
    print("| c : Calculate".ljust(29,' ')+'|')
    print("| h : Help".ljust(29,' ')+'|')
    print("| q : Quit".ljust(29,' ')+'|')
    print("="*30)

    choice = input("| Enter choice(h|c|q):".title())
    return str(choice) if choice != '' else 'h'

def extacts(entry, o):
    index = entry.find(o)
    if index != -1:
        a,b = entry.split(o)
        a = a.strip()
        b = b.strip()
    return (a,b,o)

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
    choice = menu()

    if choice == 'q':
        print('{!s}'.format('Thank You for using calculator.py!'))
        break 
    
    if choice == 'h':
        calcHelp()
        continue

    if choice == 'c':
        entry = input("Enter x operator y: ")
    
        for o in ops:
            if entry.count(o) == 1:
                x,y,operator = extacts(entry,o)
            if entry.count(o) == 2:
                x,y,operator = extacts(entry,2*o)

        if operator not in ops:
            calcHelp()
            continue
        
        a = float(x)
        b = float(y)
        
        res, err = result(a, b, operator)
        if res != False:
            print(f"{a} {operator} {b} = {res}")
        else:
            print(f"{err}")
