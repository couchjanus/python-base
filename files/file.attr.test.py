# -*- coding: utf-8 -*-
# file.attr.test.py

my_file = open("README.md", "r")
# file.name Возвращает имя файла.
print("Имя файла: ", my_file.name)

# file.mode Возвращает режим доступа, с которым был открыт файл.
print("В каком режиме файл открыт: ", my_file.mode)

my_file.close()
# file.closed Возвращает True если файл был закрыт.
print("Файл закрыт: ", my_file.closed)

# Имя файла:  README.md
# В каком режиме файл открыт:  r
# Файл закрыт:  True
