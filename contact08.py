# Contact attributes:
# id
# name
# phone_number
# favorite
# address
# note
# real_date
# real_time

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
    },
]

print("Name:", contacts[0]['name'])
print("Phone Number:", contacts[0]['phone'])


# Метод get() позволяет получить элемент по его ключу:

print("Name:", contacts[0].get('name'))
print("Phone Number:", contacts[0].get('phone'))
print("Age:", contacts[0].get('age'))
# получение значения по ключу или значения по умолчанию в случае отсутствия ключа
print(contacts[0].get('abc', 'default value'))

print(contacts[0].keys())              # список ключей
print(contacts[0].values())            # список значений
print(contacts[0].items())             # список пар ключ-значение

# Цикл по ключам
for key in contacts[0].keys():
   print(key, contacts[0][key])

# Цикл по паре ключ-значение
for k,v in contacts[0].items():
   print(k, ' =>  ', v)

# Цикл по значениям
for val in contacts[0].values():
   print(val)

contacts[0]['age'] = 27 # добавляем
print("Age: ", contacts[0]['age'])

# получение значения по ключу или значения
# по умолчанию в случае отсутствия ключа (при этом значение записывается в словарь)

contacts[0].setdefault("favorite", 0) # добавляем по умолчанию
print("Favorite: ", contacts[0]['favorite'])


print(contacts[0])
contacts[0].clear()
print(contacts[0])


contact = contacts[1].copy()
contact['age'] = 33
print(contact)
print(contacts[1])

