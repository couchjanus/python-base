# contact03.class.py
'''
 Program make a simple phonegup that can add,
 view, modify, delete and save the records
'''
# Importing libraries
from datetime import datetime, timedelta

class Person:
    """ Class Documentation """

    def __init__(self, first_name, last_name, favorite=1, note=None, mobile_phone=None, office_phone=None, private_phone=None, email=None, address=None, age=None):
        self._first_name = first_name
        self._last_name = last_name
        self._favorite = favorite
        self._note = note
        self._mobile = mobile_phone
        self._office = office_phone
        self.__private = private_phone
        self._email = email
        self.__address = address
        self._age = age
        self._date = self.__current_date()[0]
        self._time = self.__current_date()[1]

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
        return self._first_name.title() +" " + self._last_name.title()

    def add_mobile_phone(self, number):
        """ Method documentation """
        
        self._mobile = number

    def add_office_phone(self, number):
        self._office = number

    def add_private_phone(self, number):
        self.__private = number

    def add_email(self, address):
        self._email = address

    def add_note(self, note):
        self._note = note
    
    def add_favorite(self, favorite):
        self._favorite = favorite
    
    def get_private_phone(self):
        try:
            return self.self.__private
        except:
            return False

    def print_contacts(self):
        s = f'\nname: {self.full_name()}'
        if self._mobile is not None:
            s += f'\nmobile phone:  {self._mobile}'
        if self._office is not None:
            s += f'\noffice phone:   {self._office}' 
        if self.__private is not None:
            s += f'\nprivate phone:  {self.__private}' 
        if self._email is not None:
            s += f'\nemail address:  {self._email}' 
        print(s + f'\ndate:  {self._date} {self._time}' )

p1 = Person('Hugo','Boss', office_phone='767828283', email='h@cat.com')
p2 = Person('Dolche', 'Gabano', office_phone='767828292', private_phone='99999999')
p2.add_email('dg@dog.net')

print(p2) 
print(dir(p2))
print (p2.__dict__)
