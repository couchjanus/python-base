# -*- coding: utf-8 -*-
# shelve.for.file.test.py

# Либо можно открывать файл с помощью оператора with. 
# Сохраним и считаем в файл несколько объектов:
import shelve
 
FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"


# Используя цикл for, можно перебрать все значения из файла:

with shelve.open(FILENAME) as states:
    for key in states:
        print(key," - ", states[key])


