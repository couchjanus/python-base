import re

# компилирует шаблон регулярного выражения, который соответствует хотя бы одному или нескольким символам пробела.

regex = re.compile('\s+')

str = 'Функция compile преобразует регулярное выражение во внутренний формат - этот процесс называется компиляцией, а затем выполняет свою работу'

match = re.search(regex, str)
if match:
    print('found', match.group())
else:
    print('did not find')

# лучше писать так:

match = regex.search(str)
if match:
    print('found', match.group())
else:
    print('did not find')
