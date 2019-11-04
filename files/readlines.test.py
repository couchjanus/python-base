# -*- coding: utf-8 -*-
# readlines.test.py

# метод readlines() для считывания всего файла в список строк:

with open("hello.txt", "r") as file:
    contents = file.readlines()
    str1 = contents[0]
    str2 = contents[1]
    print(str1, end="")
    print(str2)

