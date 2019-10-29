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

# Создать список contacts
contacts = [
    [0, 'John Doe', 2134567, 10, 'Kyiv City, 1, Some Square', 'an anonymous party, typically the plaintiff, in a legal action', '24/10/2019', '15:38:31'], 
    [1, 'Mary Ann', 1234567, 30, 'Kyiv City, 121, Some Strit', 'Pretty Girl', '24/10/2019', '15:38:31'], 
    [2, 'Anna Lisa', 9234567, 3, 'Kyiv City, 12, Some Strit', 'Another Pretty Girl', '24/10/2019', '15:38:31']
]

# итерация списка:
for x in contacts:
   print(x)

contact = []
contact.append(len(contacts))

# name
name  = input(f'Enter Name:')
contact.append(name)
# phone_number
phone_number  = input(f'Enter Phone:')
contact.append(phone_number)
contact.append(0)
# address
address  = input(f'Enter Address:')
contact.append(address)
# note
note  = input(f'Enter Note:')
contact.append(note)

contact += current_date()
contacts.append(contact)

# итерация списка:
for x in contacts:
   print(x)
