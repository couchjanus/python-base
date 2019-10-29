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

# Создать tuple contacts
contacts = [
    (0, 'John Doe', 2134567, 10, 'Kyiv City, 1, Some Square', 'an anonymous party, typically the plaintiff, in a legal action', '24/10/2019', '15:38:31'), 
    (1, 'Mary Ann', 1234567, 30, 'Kyiv City, 121, Some Strit', 'Pretty Girl', '24/10/2019', '15:38:31'), 
    (2, 'Anna Lisa', 9234567, 3, 'Kyiv City, 12, Some Strit', 'Another Pretty Girl', '24/10/2019', '15:38:31')
]


L=[i for i in range(10)]
print([i+1 for i in L])

L1=[['a','b','c'],[1,2,3],[1.5,2.5,3.5]]
L2=[row[1] for row in L1]
print(L2)

print('_'*78)

# Из кортежа можно извлекать элементы:
print(caption[3])

# Из кортежа можно брать срезы:
print(caption[0:3])

# Однако изменять элементы кортежа нельзя:
# caption[3] = 11
# TypeError: 'tuple' object does not support item assignment

srt_capture = '| '

# итерация tuple:
for x in caption[0:3]:
    srt_capture += x.title() + ' | '
print(srt_capture)

print(id(contacts))
for x in contacts:
    print(x[0:3])
    print(id(x))

for x in contacts:
    for t in x[0:3]:
        print(t, len(str(t)))

clst = list(caption[0:3])
maxlen = [len(n) for n in clst]
print(maxlen)

maxl = []
for x in contacts:
    mx = [len(str(n)) for n in list(x[0:3])]
    maxl.append(mx)

print(maxl)

def matrixTranspose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]

print(matrixTranspose(maxl))

res = [max(lst) for lst in matrixTranspose(maxl)]
print(res)

print(max(res))

lres = max(res)

print(sum(res))

p = '| '
d = '_'
s = ' '

for x in range(lres*5+2):
    s += d
print(s)

lgup = lres//2

# clst
for i in range(len(clst)):
    p += ' '*(lgup) + clst[i].title()+ ' '*(lres - len(clst[i])) +' | '
print(p)

print(s)
p = '| '
for x in contacts:
    rlst = list(x[0:3]) 
    for i in range(len(clst)):
        p += ' '*(lgup) + str(rlst[i])+ ' '*(lres - len(str(rlst[i]))) +' | '
    print(p)
    p = '| '

print(s)
