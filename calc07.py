#! /usr/bin/env python
# coding: utf

str_var = "Calculator"
print("Hello, ", str_var)

a = b = 2
print("a: ", a)
print("b: ", b)
print("a + b = ", a + b)

# Функция input() с аргументом-приглашением
a = int(input("Enter a: "))
print("a: ", a)
b = int(input("Enter b: "))
print("b: ", b)

if b != 0:
    print("a / b = ", a / b)
else:
    print("Oops, division by zero")
