# 02.py
# метод match ищет по заданному шаблону в начале строки. 

import re

fatCat = """I once had a big fat cat
    Who caught a big friendly rat.
    She played with it like a toy
    It gave her so much joy
    That she spared it and that was that.

    """
# r перед строкой шаблона - это сырая строка в Python

result = re.match(r'I', fatCat)
if result == None:
    print("Match not found")
else:
    print("Match found")
    print(result)

# Искомая подстрока найдена. Результат:
# <re.Match object; span=(0, 1), match='I'>

# match() вернет Match Object

# Match Object имеет несколько методов и атрибутов, наиболее важными из которых являются:
# group()- Вернуть строку, совпавшую с регулярным выражением
# start() - Вернуть позицию начала совпадения
# end() - Вернуть позицию конца совпадения
# span() - Вернуть кортеж (start, end) позиций совпадения

print(result.group())

# метод match() проверяет совпадения только с начала строки - start() всегда будет возвращать 0. 

print (result.start(), result.end())

print(result.span())

# список специальных символов:

# \A 	Начало строки; эквивалент ^
# \b 	Начало слова
# \B 	Не начало слова
# \d 	Цифра; расширенный вариант [0-9]
# \D 	Не цифра; «отрицание» \d
# \s 	Пробельный символ; расширенный вариант [ \t\n\r\f\v]
# \S 	Не пробельный символ; «отрицание» \s
# \w 	«Буква» в слове расширенный вариант [a-zA-Z0-9_]
# \W 	Не «буква»; «отрицание» \w
# \Z 	Конец строки; эквивалент $

print(re.match(r'\Aab', 'abcd'))
print(re.match(r'\Aab', 'dabcd'))