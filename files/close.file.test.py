# -*- coding: utf-8 -*-
# close.file.test.py

my_file = open("README.md", "r")

print(f"Имя файла: {my_file.name}")

# Python автоматически закрывает файл 
# если файловый объект к которому он привязан присваивается другому файлу. 
# Однако, хорошей практикой будет вручную закрывать файл командой close().

my_file = open("LICENSE", "r")

print(f"Имя файла: {my_file.name}")
print(f"Файл {my_file.name} закрыт: {my_file.closed}")

my_file.close()
print(f"А теперь файл {my_file.name} закрыт: {my_file.closed}")
