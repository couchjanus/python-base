# compile/02.py
import re

str = 'Функция compile преобразует регулярное выражение во внутренний формат - этот процесс называется компиляцией, а затем compile выполняет свою работу'

pattern = re.compile('compile')
result = pattern.findall(str)

print(result)

pattern1 = re.compile('[a-z]+')

# Пустая строка не будет соответствовать pattern1, потому что + означает повторение «один или больше» раз. match() в этом случае должен вернуть None:

print(pattern1.match(""))

# findall() возвращает список совпавших подстрок:

pattern2 = re.compile('\d+')

print(pattern2.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping'))

# Вставив символ "^" сразу после открытия квадратных скобок вы создаете отрицание:

regex = re.compile(r'[^аяоёуюыиэеАЯОЁУЮЫИЭЕ]') 
# теперь мы ищем все не гласные буквы

print(regex.findall('Все гласные буквы'))

# Мы можем использовать знак "^" в начале шаблона для поиска в начале строки(совпадение должно произойти в начале строки), а "$" для поиска в конце строки(совпадение должно произойти в конце строки):

regex = re.compile(r'^Hello')
mo = regex.search('Hello world!')
print(mo.group())

mo = regex.search('He said Hello')
# print(mo.group())

regex = re.compile(r'Hello$')

mo = regex.search('Hello world!')
# print(mo.group())

mo = regex.search('He said Hello')
print(mo.group())
