# contact01.class.py

class Person:
    """ Class Documentation """

    def __init__(self, first_name, last_name, favorite=1, note=None, mobile_phone=None, office_phone=None, private_phone=None, email=None):
        self._first_name = first_name
        self._last_name = last_name
        self._favorite = favorite
        self._note = note
        self._mobile = mobile_phone
        self._office = office_phone
        self.__private = private_phone
        self._email = email

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

    def print_contacts(self):
        s = f'\nname: {self._first_name} {self._last_name}'
        if self._mobile is not None:
            s += f'\nmobile phone:  {self._mobile}'
        if self._office is not None:
            s += f'\noffice phone:   {self._office}' 
        if self.__private is not None:
            s += f'\nprivate phone:  {self.__private}' 
        if self._email is not None:
            s += f'\nemail address:  {self._email}' 
        print(s)

p1 = Person('Hugo','Boss', office_phone='767828283', email='h@cat.com')
print("_email: ", p1._email)


p2 = Person('Dolche', 'Gabano', office_phone='767828292', private_phone='99999999')
p2.add_email('dg@dog.net')

# print("__private: ", p2.__private)

phone_book = [p1, p2]

for person in phone_book:
    person.print_contacts()
