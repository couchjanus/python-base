# -*- coding: utf-8 -*-
# contact17.py

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
#         print("Имя: {: >4}".format(contact['first_name']), "{: >4}".format(contact['last_name']), "Возраст: {: >2}".format(contact['age']), "Phone: {: >3}".format(contact['phone']))

with open(FILENAME, "rb") as file:
    try:
        while True:
            data.append(pickle.load(file))
    except EOFError:
        pass
    print('\n\t')
    print('\n'.join(['\t'.join([str(cell) + ": " + str(contact[cell]) + "\n" for cell in contact]) for contact in data]))
