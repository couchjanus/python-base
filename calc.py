#! /usr/bin/env python
# coding: utf

print("Super Calc")

running = True

while running:

    # Convert strings into integers
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    # Store the user input an operator
    o = input('Enter Operator: ')

    if o == 'q':
        print('Programm done.')
        running = False # это останавливает цикл while
    if o == "+":
        print("a + b = ", a + b)
    elif o == '-':
        print("a - b = ", a - b)
    elif o == '*':
        print("a * b = ", a * b)
    elif o == '/':
        if b != 0:
            print("a / b = ", a / b)
        else:
            print("Oops, division by zero")
    # If none of the above conditions were true then execute this by default
    else:
        print("Use either + - * / or % next time")
