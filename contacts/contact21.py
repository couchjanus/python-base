# -*- coding: utf-8 -*-
# contact21.py remove

'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
# Importing libraries
from datetime import datetime, timedelta
import pickle
 
FILENAME = "contacts.dat"

titles = (
    'Select operation:',
    "Usage operation:"
    )

choices = (
    "Help",
    'Print Phone Numbers',
    'Add a Phone Number',
    'Remove a Phone Number',
    'Clear All Records',
    'Lookup a Phone Number',
    'Save Phone Numbers',
    "Quit"
    )

helpers = (
    'Display this usage message',
    'Print Phone Numbers',
    'Add a Phone Number',
    'Remove a Phone Number',
    'Clear All Records',
    'Lookup a Phone Number',
    'Save Phone Numbers',
    'Exit programm'
    )

lookup = (
    "first_name", 
    "last_name", 
)

def printMenu(w, j, obj):
    gup = (': ', '| ')

    print("_"*(w+7))
    print(gup[1] + titles[j].ljust(w+3, ' ') + gup[1][::-1])

    for item in obj:
        print(
            gup[1] + item[0].lower() + gup[0] +
            item.ljust(w, ' ') + gup[1][:: -1]
            )

    print("="*(w+7))

def menu():
    tupleLen = [len(i) for i in choices]
    width = max(max(tupleLen), len(titles[0]))

    print('PhoneBook'.upper().center(width+7, '='))
    printMenu(width, 0, choices)

    choiceList = [item[0].lower() for item in choices]
    choiceList = ' | '.join(choiceList)

    choice = input("Enter choice "+choiceList+':>')
    return str(choice) if choice != '' else 'h'

def myhelp():
    list1 = list()
    for i in range(len(helpers)):
        list1.append(choices[i]+' - ' + helpers[i])

    listLen = [len(i) for i in list1]
    printMenu(max(listLen), 1, list1)

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

# lambda
full_name = lambda first_name, last_name: first_name.title() +" " + last_name.title()

format_cell = lambda cell: [t.title() for t in cell.split("_")]

def print_contacts():
    data = []
    print("All Contacts in PhoneBook:")
    with open(FILENAME, "rb") as file:
        try:
            while True:
                data.append(pickle.load(file))
        except EOFError:
            pass
        for contact in data:
            print(f"{data.index(contact)}\tИмя: {full_name(contact['first_name'], contact['last_name'])}\tPhone: {contact['phone']}")

# remove
def delete_contact(filename, id):
    contacts = []
    with open(filename, "rb") as file:
        try:
            while True:
                contacts.append(pickle.load(file))
        except EOFError:
            pass
    try:
        del contacts[id]
        
        with open(filename, "wb") as file:
            for c in contacts:
                pickle.dump(c, file)
        return id
    except KeyError:
        print("{contact} doesn't exist in db".format(contact=id))

# clear
def clear_database():
    file = open(FILENAME, 'w')
    file.close()

# save
def save_object(obj, filename):
    with open(filename, 'ab') as file:
        pickle.dump(obj, file)

# list
def print_contact(look):
    for lookKey in lookup:
        if lookKey.startswith(look):
            serchKey = lookKey
    key = 'phone'
    
    search = input("Enter Search String " + ':>')

    contacts = []
    
    with open(FILENAME, "rb") as file:
        try:
            while True:
                contacts.append(pickle.load(file))
        except EOFError:
            pass
    
    for item in contacts:
        if search.title() in item.get(serchKey):
            print("Contact in PhoneBook:")
            print(f"# {contacts.index(item)}")
            print(f"{item.get('first_name')} {item.get('last_name')} has a phone number: {item.get(key)}")
            
            print(f"Address: {item.get('address')}")
            print(f"Age: {item.get('age')}")
            print(f"Note: {item.get('note')}")
            print(f"Added At: {item.get('date')} T{item.get('time')}")
            print

# look
def look_contact():
    fieldListHelp = [''.join([item[0], ': for ', ' '.join(format_cell(item))]) for item in lookup]
    fieldList = [item[0] for item in lookup]
    look = input("Enter Field "+' or '.join(fieldListHelp)+':>')
    return str(look) if (look != '' and look in fieldList) else 'h'

# create
def create_item():
    print("Add New Record To PhoneBook")
    first_name = input("First Name: ")
    last_name = input("Last Name: ") 
    phone = input("Phone Number: ")
    address = input("Address: ")
    age = input("Age: ")
    note = input("Note: ")

    save_object(add_contact(first_name, last_name, phone, address, age, note), FILENAME)

# main
while True:
 
    choice = menu()

    if choice == 'q':
        print('{!s:#^40}'.format('Thankyou for using phoneBook.py!'))
        break
    if choice == 'h':
        myhelp()
        continue

    if choice == 'p':
        print_contacts()

    elif choice == 'a':
        create_item()

    elif choice == 'r':
        print("Choice Record Id To Remove")
        print_contacts()
        id = int(input("Record Id: "))
        remove_id = delete_contact(FILENAME, id)
        print(f'Record {remove_id} Removed Successfully!')

    elif choice == 'c':
        clear_database()
        print(f'All Records Removed Successfully!')
        print_contacts()

    elif choice == 'l':
        look = look_contact()
        if look == 'h':
            print('Use f for First Name or l for Last Name')
        else:
            print_contact(look)
    else:
        myhelp()
        continue
