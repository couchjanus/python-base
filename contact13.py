'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
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

# Contact attributes:
# id
# name
# phone
# favorite
# address
# age
# note
# date
# time

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


# Dict contacts

contacts = {
    0: {
        "id": 0,
        "name": 'John Doe', 
        "phone": 2134567, 
        "favorite": 10, 
        "address": 'Kyiv City, 1, Some Square', 
        "age": 22,
        "note": 'an anonymous party, typically the plaintiff, in a legal action', 
        "date": '24/10/2019', 
        "time": '15:38:31'   
    },
    1: {
        "id": 1,
        "name": 'Mary Ann', 
        "phone": 1234567, 
        "favorite": 30, 
        "address": 'Kyiv City, 121, Some Strit', 
        "age": 19,
        "note": 'Pretty Girl', 
        "date": '24/10/2019', 
        "time": '15:10:31'   
    },
    2: {
        "id": 2,
        "name": 'Anna Lisa', 
        "phone": 9234567, 
        "favorite": 3, 
        "address": 'Kyiv City, 11, Some Strit', 
        "age": 25,
        "note": 'Another Pretty Girl', 
        "date": '24/10/2019',
        "time": '15:40:31'
    }
}

def print_contacts(contacts):
    print("All Contacts in PhoneBook:")
    for id in contacts:
        print("Id:\t", id, "\t", "Name:\t", contacts[id]['name'], "\t", "Number:\t", contacts[id]['phone'])
    print

def add_contact(name, phone, address, age, note):
    d = {
        'id': len(contacts),
        'name': name,
        'phone': phone,
        'address': address,
        "favorite": 1, 
        "age": age,
        "note": note, 
        "date": current_date()[0],
        "time": current_date()[1]
        }

    contacts.update({len(contacts): d})


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

def del_contact(id):
    # del contacts[id] # remove contacts[id]
    # проверка наличия ключа
    if id in contacts:
        del contacts[id] # remove contacts[id]

def pop_contact(id):
    # проверка наличия ключа
    if id in contacts:
        return contacts.pop(id) # pop contacts[id]
    # return contacts.pop(id) # pop contacts[id]

def clear_contacts():
    contacts.clear()

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

# gup = (': ', '| ')
# print(gup[1][:: -1]) # |

while True:

    choice = menu()

    if choice == 'q':
        print('{!s:#^40}'.format('Thankyou for using phoneBook.py!'))
        break
    if choice == 'h':
        myhelp()
        continue
    if choice == 'p':
        print_contacts(contacts)
    elif choice == 'a':
        print("Add New Record To PhoneBook")
        print("Add New Record To PhoneBook")
        name = input("First Name: ")
        phone = int(input("Phone Number: "))
        address = input("Address: ")
        age = int(input("Age: "))
        note = input("Note: ")

        add_contact(name, phone, address, age, note)
    elif choice == 'r':
        print("Choice Record Id To Remove")
        print_contacts(contacts)
        id = int(input("Record Id: "))
        remove_contact = pop_contact(id)
        print(f'Record {remove_contact} Removed Successfully!')
    elif choice == 'c':
        clear_contacts()
        print(f'All Records Removed Successfully!')
        print_contacts(contacts)

    else:
        myhelp()
        continue

