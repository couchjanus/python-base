# -*- coding: utf-8 -*-
# shelve.keys.file.test.py

# Либо можно открывать файл с помощью оператора with. 
# Сохраним и считаем в файл несколько объектов:
import shelve
 
FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"

# Метод keys() возвращает все ключи из файла, а метод values() - все значения:
with shelve.open(FILENAME) as states:
 
    for city in states.keys():
        print(city)        # London Paris Berlin Madrid 
    print()

    for country in states.values():
        print(country)     # Great Britain France Germany Spain 

