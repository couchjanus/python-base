#Contact attributes:
# id
# name
# phone_number
# favorite
# address
# note
# created_at

# https://docs.python.org/3/library/datetime.html
# Importing libraries
from datetime import datetime, timedelta

# Current datetime
now = datetime.now()
print('Now = ' + str(now))

# Yesterday
one_day = timedelta(days=1)
yesterday = now - one_day
print('Yesterday = ' + str(yesterday))

# Last week
one_week = timedelta(weeks=1)
last_week = now - one_week
print('Last week = ' + str(last_week))

# Formatting date
day = now.day
month = now.month
year = now.year
print(f'Date = {day}/{month}/{year}')

# Formatting time
hour = now.hour
minute = now.minute
second = now.second
print(f'Time = {hour}:{minute}:{second}')

# Input date
# input_date = input('Type a date with the format: (dd/mm/yyyy)\n')
# real_date = datetime.strptime(input_date, '%d/%m/%Y')
# print('Your date is {0}'.format(str(real_date)))

# Input time
# input_time = input('Type a time with the format: (hh:mm)\n')
# real_time = datetime.strptime(input_time, '%H:%M')
# print('Your time is {0}'.format(str(real_time)))

# Создать список contact
contact = [0, 'John Doe', 2134567, 10, 'Kyiv City, 1, Some Square', 'an anonymous party, typically the plaintiff, in a legal action']

real_date = f'{day}/{month}/{year}'
real_time = f'{hour}:{minute}:{second}'

date = [real_date, real_time]
print(contact + date)

contacts = contact + date
print(contacts)

# простая итерация списка:
print(f'простая итерация списка:')
for x in contacts:
   print(x)

print()
# reverse() — реверс списка:
# Отсортировать список по убыванию
contacts.reverse()
print(f'Отсортировать список по убыванию: ', contacts)

# сортированная итерация:
L = [5, 4, 1, 2, 3]
print()
print(f'сортированная итерация:')
for x in sorted(L):
   # for x in sorted(contacts):
   # sorted() function can't sort different types of variables.
   # If we try sorted([1, "a string"]), you will get the error, but if we try sorted([5, 2]), it will work.
   print(x)

print()
# Отсортировать список по убыванию
L.reverse()
print(f'Отсортировать список по убыванию: ', L)

print()
# sort() — Отсортировать список:
L.sort()
print(f'Отсортировать список: ', L)

print()
print(f'итерация в обратном порядке:')
# итерация в обратном порядке:

for x in reversed(contacts):
   print(x)
print()
