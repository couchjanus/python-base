# contact05.class.py
'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
# Importing libraries
from datetime import datetime, timedelta
import pickle

class Person:
    """ Class Documentation """

    def __init__(self, first_name, last_name, favorite=1, note=None, mobile_phone=None, office_phone=None, private_phone=None, email=None, address=None, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite = favorite
        self.note = note
        self.mobile = mobile_phone
        self.office = office_phone
        self.private = private_phone
        self.email = email
        self.address = address
        self.age = age
        self.date = self.__current_date()[0]
        self.time = self.__current_date()[1]

    def __current_date(self):
        now = datetime.now()
        day = now.day
        month = now.month
        year = now.year
        hour = now.hour
        minute = now.minute
        second = now.second
        return [f'{day}/{month}/{year}', f'{hour}:{minute}:{second}']
    
    def full_name(self):
        return self.first_name.title() +" " + self.last_name.title()

    def add_mobile_phone(self, number):
        """ Method documentation """
        
        self.mobile = number

    def add_office_phone(self, number):
        self.office = number

    def add_private_phone(self, number):
        self.private = number

    def add_email(self, address):
        self.email = address

    def add_note(self, note):
        self.note = note
    
    def add_favorite(self, favorite):
        self.favorite = favorite
    
    def get_private_phone(self):
        try:
            return self.self.private
        except:
            return False

    def print_contacts(self):
        s = f'\nname: {self.full_name()}'
        if self.mobile is not None:
            s += f'\nmobile phone:  {self.mobile}'
        if self.office is not None:
            s += f'\noffice phone:   {self.office}' 
        if self.private is not None:
            s += f'\nprivate phone:  {self.private}' 
        if self.email is not None:
            s += f'\nemail address:  {self.email}' 
        print(s + f'\ndate:  {self.date} {self.time}' )

    def save(self, obj, filename):
        with open(filename, 'ab') as file:
            pickle.dump(obj, file)

FILENAME = "contacts.dat"

print("Add New Record To PhoneBook")

first_name = input("First Name: ")
last_name = input("Last Name: ") 
office_phone = input("Office Phone Number: ")

person = Person(first_name, last_name)
person.add_office_phone(office_phone)

person.save(person.__dict__, FILENAME)

data = []

with open(FILENAME, "rb") as file:
    try:
        while True:
            data.append(pickle.load(file))
    except EOFError:
        pass
    for contact in data:
        print(f"Имя: {contact['first_name']} {contact['last_name']} \tOffice phone: {contact['office']}")
