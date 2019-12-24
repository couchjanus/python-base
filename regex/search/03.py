# search 03.py
import re

# re.search('a', 'bab')
# re.search('^a', 'bab')
# re.search('^a$', 'bab')
# re.search('a$', 'bab')
# re.search('^.a.$', 'bab')
# re.search('a?', 'bbb')
# re.search('a?', 'bab')
# re.search('a+', 'bab')
# re.search('a+', 'baaab')
# re.search('a*', 'baaab')
# re.search('ba*b', 'baaab')
# re.search('ba+b', 'baaab')
# re.search('ba?b', 'baaab')
# re.search('a{2}', 'baaab')
# re.search('a{3}', 'baaab')
# re.search('a{4}', 'baaab')
# re.search('a{1}', 'baaab')
# re.search('a{1,2}', 'baaab')
# re.search('a{1,3}', 'baaab')
# re.search(r'\*', r'*')
# re.search(r'[abc]', r'0123ccaabb275')
# re.search(r'[abc]?', r'0123ccaabb275')
# re.search(r'[abc]+', r'0123ccaabb275')
# re.search(r'[0-9]{4}[abc]+[0-9]{3}', r'0123ccaabb275')
# re.search(r'[0-9]{4}[^0-9]+[0-9]{3}', r'0123ccaabb275')
# re.search(r'a|b', r'ccadd')
# re.search(r'a|b', r'ccbdd')


# Специальный символ
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


re.search(r'\bbbb', 'abbba bbb ccc')
re.search(r'\Bbbb', 'abbba bbb ccc')
re.search(r'\d+', 'ab123cd')
re.search(r'\D+', 'ab123cd')


re.search(r'\w+', 'ab123cd')
re.search(r'\W+', 'ab123cd')
re.search(r'\w+', 'ab123cd  aaa')
re.search(r'\W+', 'ab123cd  aaa')
re.search(r'aa\Z', 'bbaa')
re.search(r'aa\Z', 'bbaab')

