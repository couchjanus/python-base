# -*- coding: utf-8 -*-
# shelve.states.file.test.py

# Либо можно открывать файл с помощью оператора with. 
# Сохраним и считаем в файл несколько объектов:
import shelve

FILENAME = "states" 
# FILENAME = "states2"
with shelve.open(FILENAME) as states:
    states["London"] = "Great Britain"
    states["Paris"] = "France"
    states["Berlin"] = "Germany"
    states["Madrid"] = "Spain"
    states["Kiev"] = "Ukraine"
 
with shelve.open(FILENAME) as states:
    print(states["London"])
    print(states["Madrid"])
    print(states["Kiev"])

