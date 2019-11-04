# -*- coding: utf-8 -*-
# seek.test.py

my_file = open("some.txt", "r")
print(my_file.read(10))
print("Мы находимся на позиции: ", my_file.tell())
# Возвращаемся в начало
my_file.seek(0)
print(my_file.read(10))
my_file.close()
