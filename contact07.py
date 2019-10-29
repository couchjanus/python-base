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

# tuple caption
caption = ('id', "name", "phone", "favorite", "address", "note", "date", "time")

# tuple contacts
contacts = [
    (0, 'John Doe', 2134567, 10, 'Kyiv City, 1, Some Square', 'an anonymous party, typically the plaintiff, in a legal action', '24/10/2019', '15:38:31'), 
    (1, 'Mary Ann', 1234567, 30, 'Kyiv City, 121, Some Strit', 'Pretty Girl', '24/10/2019', '15:38:31'), 
    (2, 'Anna Lisa', 9234567, 3, 'Kyiv City, 12, Some Strit', 'Another Pretty Girl', '24/10/2019', '15:38:31')
]

def matrixTranspose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]

def print_table():
    caption_lst = list(caption[0:3])
    maxlen_caption = [len(n) for n in caption_lst]

    maxlen_contacts = []
    for x in contacts:
        mx = [len(str(n)) for n in list(x[0:3])]
        maxlen_contacts.append(mx)

    res = [max(lst) for lst in matrixTranspose(maxlen_contacts)]

    len_res = max(res)
    p = '| '
    d = '_'
    s = ' '

    for x in range(len_res*5+2):
        s += d
    print(s)

    lgup = len_res//2

    # caption_lst
    for i in range(len(caption_lst)):
        p += ' '*(lgup) + caption_lst[i].title()+ ' '*(len_res - len(caption_lst[i])) +' | '
    print(p)

    print(s)
    p = '| '
    for x in contacts:
        rlst = list(x[0:3]) 
        for i in range(len(caption_lst)):
            p += ' '*(lgup) + str(rlst[i])+ ' '*(len_res - len(str(rlst[i]))) +' | '
        print(p)
        p = '| '
    print(s)

print_table()

contact = []
contact.append(len(contacts))

# # name
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
contacts.append(tuple(contact))

print_table()
