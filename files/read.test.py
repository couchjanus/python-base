# -*- coding: utf-8 -*-
# read.test.py

# Например, прочтем созданный нами файл some.txt:

my_file = open("some.txt")
my_string = my_file.read()
print("Было прочитано:")
print(my_string)
my_file.close()

with open("hello.txt", "r") as file:
    for line in file:
        print(line)
