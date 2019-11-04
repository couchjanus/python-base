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

# tuple caption
caption = ('id', "name", "phone", "favorite", "address", "note", "date", "time")

# List dicts contacts
contacts = [
    {
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
    {
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
    {
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
]

def print_contacts(contacts):
    print("All Contacts in PhoneBook:")
    for id in range(len(contacts)):
        print("Name:\t", contacts[id]['name'], "\t", "Number:\t", contacts[id]['phone'])
    print

print_contacts(contacts)

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

    contacts.append(d)

print("Add New Record To PhoneGap")
name = input("First Name: ")
phone = int(input("Phone Number: "))
address = input("Address: ")
age = int(input("Age: "))
note = input("Note: ")
add_contact(name, phone, address, age, note)

print_contacts(contacts)

