#Contact attributes:
# name
# phone_number
# address

contacts = []
contacts = ['Mary Ann', 1234567, 'Some City, 1, Some Strit']
print(contacts)

contacts = list()
contacts = ['Mary Ann', 1234567, 'Some City, 1, Some Square']

print(contacts)

print(contacts[2])


# Для замены значений используется обращение по индексу с последующим присвоением нового значения.

contacts[2] = 'Kyiv City, 121, Some Square'
print(contacts[2])

# Списки могут содержать объекты любых типов, изменять содержимое и размер.

"""
    an anonymous party, typically the plaintiff, in a legal action.

    "For prosecutors, indicting John Does through their DNA might seem more than fair."
"""
# len() — длина списка:

contacts = ['John Doe', 2134567, 'Kyiv City, 1, Some Square']
print(contacts)
print(len(contacts))

# Добавить элемент в конец списка
contacts.append('an anonymous party, typically the plaintiff, in a legal action')
print(contacts)
print(len(contacts))

# Элемент можно добавить в произвольную позицию списка с помощью метода insert:
contacts.insert(0, 0)
print(contacts)
print(len(contacts))

# Вставить в позицию 3 списка элемент со значением 10
contacts.insert(3, 10)
print(contacts)
print(len(contacts))
print()
# Для проверки, является ли элемент членом списка, есть оператор in:
print('Contacts contains 2?: ', 2 in contacts)
print('Contacts contains 10?: ', 10 in contacts)

print()
# index() — взять элемент списка по индексу:
print('Index of item = 10: ', contacts.index(10))

# count() — подсчет числа повторов какого-то элемента:
contacts.insert(3, 10)
print('Count item = 10 into contacts: ', contacts.count(10))
print('Index of item = 10: ', contacts.index(10))
print()
# remove() — удаление конкретного элемента:
contacts.remove(10)
print('Count item = 10 into contacts after remove: ', contacts.count(10))
print('Index of item = 10 after remove: ', contacts.index(10))
print()
# del — удаление конкретного элемента:
contacts.insert(3, 10)
index = int(contacts.index(10))
print('Index of item = 10: ', index)

del contacts[index]
print('Count item = 10 into contacts after del: ', contacts.count(10))
print('Index of item = 10 after del: ', contacts.index(10))

print()
print(f'if contacts.count(10)>1')
index = int(contacts.index(10))
print('Index of item = 10: ', index)
if contacts.count(10)>1:
    del contacts[index]
print('Count item = 10 into contacts after del: ', contacts.count(10))
print('Index of item = 10 after del: ', contacts.index(10))

print()
contacts_2 = [1, 2, 3]
# Объединить списки contacts_2 и [4, 5] [6, 7]
print('List contacts_2: ', contacts_2)
contacts_2 += [4, 5]
print('Concatenation contacts_2 and [4, 5]', contacts_2)
contacts_2 += [6, 7]
print('Concatenation contacts_2 and [6, 7]', contacts_2)

# extend() — аналогичен append(), добавляет последовательность элементов:
contacts_2.extend([6, 7])
print('Extend contacts_2 and [6, 7]', contacts_2)
print()
# При удалении списка с помощью del, или сборщика мусора, его опустошенный объект кешируется и используется в последующем для создания нового списка.
print(f'Id contacts: {id(contacts)}')
del contacts

# Далее предполагается, что сборка мусора уже прошла.
contacts_1 = []
print(f'Id contacts_1: {id(contacts_1)}')   
del contacts_1

contacts_2 = [4, 5]
print(f'Id contacts_2: {id(contacts_2)}')   
contacts_2.extend([6, 7])

contacts_3 = []
print(f'Id contacts_3: {id(contacts_3)}')   
del contacts_3

contacts_4 = []
print(f'Id contacts_4: {id(contacts_4)}')   
