# -*- coding: utf-8 -*-
# readline.test.py

# вызовем метод readline() для чтения отдельных строк:
with open("hello.txt", "r") as file:
    str1 = file.readline()
    print(str1, end="")
    str2 = file.readline()
    print(str2)

# Метод readline можно использовать для построчного считывания файла в цикле while:
with open("hello.txt", "r") as file:
    line = file.readline()
    while line:
        print(line, end="")
        line = file.readline()
