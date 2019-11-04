# -*- coding: utf-8 -*-
# os.exists.test.py

import os

cwd = os.getcwd()
print(cwd)

# В метод os.path.exists(path) передается путь, который необходимо проверить

filename = input("Введите путь к файлу: ")

if os.path.exists(filename):
    print("Указанный файл существует") 
else:
    print("Файл не существует") 
