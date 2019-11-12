# -*- coding: utf-8 -*-
# contact18.py

'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''

import pickle
 
FILENAME = "contacts.dat"

# Importing libraries
from datetime import datetime, timedelta

def current_date():
    # Current datetime
    now = datetime.now()
    # Formatting date
    day = now.day
    month = now.month
    year = now.year
    # Formatting time
    hour = now.hour
    minute = now.minute
    second = now.second
    return [f'{day}/{month}/{year}', f'{hour}:{minute}:{second}']

def add_contact(first_name, last_name, phone, address, age, note):
    d = {
        "first_name": first_name, 
        "last_name": last_name, 
        'phone': phone,
        'address': address,
        "favorite": 1, 
        "age": age,
        "note": note, 
        "date": current_date()[0],
        "time": current_date()[1]
    }
    return d

data = []

full_name = lambda first_name, last_name: first_name.title() +" " + last_name.title()

with open(FILENAME, "rb") as file:
    try:
        while True:
            data.append(pickle.load(file))
    except EOFError:
        pass
    for contact in data:
        print("Имя:", full_name(contact['first_name'], contact['last_name']), "\tВозраст:", contact["age"], "\tPhone:", contact["phone"])

# print("Add New Record To PhoneBook")
# first_name = input("First Name: ")
# last_name = input("Last Name: ") 
# phone = input("Phone Number: ")
# address = input("Address: ")
# age = input("Age: ")
# note = input("Note: ")

# with open(FILENAME, "ab") as file:
#     pickle.dump(add_contact(first_name, last_name, phone, address, age, note), file)

# with open(FILENAME, "rb") as file:
#     try:
#         while True:
#             data.append(pickle.load(file))
#     except EOFError:
#         pass
#     print('\n\t')
#     print('\n'.join(['\t'.join([str(cell) + ": " + str(contact[cell]) + "\n" for cell in contact]) for contact in data]))

format_cell = lambda cell: [t.title() for t in cell.split("_")]

# with open(FILENAME, "rb") as file:
#     try:
#         while True:
#             data.append(pickle.load(file))
#     except EOFError:
#         pass
#     print('\n\t')

#     print('\n'.join(['\t'.join([' '.join(format_cell(cell)) + ": " + str(contact[cell]) + "\n" for cell in contact]) for contact in data]))


# with open(FILENAME, "rb") as file:
#     data = pickle.load(file)
#     cnt = 0
#     for item in data:
#         print('The data ', cnt, ' is : ', item)
#         cnt += 1
#     print(cnt)

