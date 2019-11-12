# -*- coding: utf-8 -*-
# contact16.py

'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
import pickle
 
FILENAME = "contacts.dat"

data = []
# with open(FILENAME, "rb") as file:
#     try:
#         while True:
#             data.append(pickle.load(file))
#     except EOFError:
#         pass
#     for contact in data:
#         print("Имя:", contact['first_name'], "\tВозраст:", contact["age"], "\tPhone:", contact["phone"])

with open(FILENAME, "rb") as file:
    try:
        while True:
            data.append(pickle.load(file))
    except EOFError:
        pass
    for contact in data:
        print("Имя: {: >4}".format(contact['first_name']), "{: >4}".format(contact['last_name']), "Возраст: {: >2}".format(contact['age']), "Phone: {: >3}".format(contact['phone']))
