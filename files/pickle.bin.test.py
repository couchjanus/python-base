# -*- coding: utf-8 -*-
# pickle.bin.test.py

# надо сохранить два объекта:

import pickle
 
FILENAME = "user.dat"
 
name = "Tom"
age = 19

# С помощью функции dump последовательно записываются два объекта. 

with open(FILENAME, "wb") as file:
    pickle.dump(name, file)
    pickle.dump(age, file)

# При чтении файла последовательно посредством функции load мы можем считать эти объекты.
#  

with open(FILENAME, "rb") as file:
    name = pickle.load(file)
    age = pickle.load(file)
    print("Имя:", name, "\tВозраст:", age)
