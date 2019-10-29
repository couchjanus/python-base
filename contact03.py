#Contact attributes:
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

# Создать вложенные списки
# Создать список contacts
contacts = []

# Создать список contact
contact = [0, 'John Doe', 2134567, 10, 'Kyiv City, 1, Some Square', 'an anonymous party, typically the plaintiff, in a legal action']
contact += current_date()
contacts.append(contact)

contact = [1, 'Mary Ann', 1234567, 30, 'Kyiv City, 121, Some Strit', 'Pretty Girl']
contact += current_date()
contacts.append(contact)


# sort() — сортировка списка:
# Отсортировать список по возрастанию
contacts.sort()
print(contacts)

# итерация списка:
for x in contacts:
   print(x)

contacts.reverse()
print(contacts)

# итерация списка:
for x in sorted(contacts):
   print(x)
   
# max() — максимальный элемент списка:
print(f'максимальный элемент списка: ', max(contacts))

# min() — минимальный элемент списка:
print(f'минимальный элемент списка: ',min(contacts))

print('='*78)
contact = [2, 'Anna Lisa', 9234567, 3, 'Kyiv City, 12, Some Strit', 'Another Pretty Girl']
contact += current_date()
contacts.append(contact)
print(contacts)
print('='*70)

# Удалить из списка элемент с индексом 2
cpop = contacts.pop(2)
print(f'Удалить из списка элемент с индексом 2: ', cpop)
print(contacts)
print('='*70)

cpop = contacts.pop()
print(f'Удалить из списка элемент с индексом len-1: ', cpop)
print(contacts)
