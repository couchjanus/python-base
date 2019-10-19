#! /usr/bin/env python
# coding: utf

str_var = "Calculator"
print("Hello, ", str_var)

a = b = 2
print("a: ", a)
print("b: ", b)
print("a + b = ", a + b)

a = input()
print("a: ", a)
b = input()
print("b: ", b)


# Функция input() с аргументом-приглашением

a = input("Enter a: ")
print("a: ", a)
b = input("Enter b: ")
print("b: ", b)

print(1 <= a < 10 and 1 <= b < 20)
print(a < b and b < 10 or b >= 1)

# print("a: ", a)
# print("b: ", b)
# print("a + b = ", a / b)