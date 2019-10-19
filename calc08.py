#! /usr/bin/env python
# coding: utf

str_var = "Calculator"
print("Hello, ", str_var)

a = int(input("Enter a: "))
print("a: ", a)
b = int(input("Enter b: "))
print("b: ", b)
o = input("Enter o: ")
print("o: ", o)

# Выровнено по открывающему разделителю
if o == '+':
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
else:
    print("Oops, not operation yet")
