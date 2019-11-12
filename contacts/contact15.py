# -*- coding: utf-8 -*-
# contact15.py

'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
import pickle
 
FILENAME = "contacts.dat"

# Dump contacts

contacts = [
    {
        "first_name": 'John', 
        "last_name": 'Doe', 
        "phone": 2134567, 
        "favorite": 10, 
        "address": 'Kyiv City, 1, Some Square', 
        "age": 22,
        "note": 'an anonymous party, typically the plaintiff, in a legal action', 
        "date": '24/10/2019', 
        "time": '15:38:31'   
    },
    {
        "first_name": 'Mary', 
        "last_name": 'Ann', 
        "phone": 1234567, 
        "favorite": 30, 
        "address": 'Kyiv City, 121, Some Strit', 
        "age": 19,
        "note": 'Pretty Girl', 
        "date": '24/10/2019', 
        "time": '15:10:31'   
    },
    {
        "first_name": 'Anna', 
        "last_name": 'Lisa', 
        "phone": 9234567, 
        "favorite": 3, 
        "address": 'Kyiv City, 11, Some Strit', 
        "age": 25,
        "note": 'Another Pretty Girl', 
        "date": '24/10/2019',
        "time": '15:40:31'
    }
]

with open(FILENAME, "wb") as file:
    for c in contacts:
        pickle.dump(c, file)

data = []
with open(FILENAME, "rb") as file:
    try:
        while True:
            data.append(pickle.load(file))
    except EOFError:
        pass
    for contact in data:
        print("Имя:", contact['first_name'], "\tВозраст:", contact["age"], "\tPhone:", contact["phone"])
