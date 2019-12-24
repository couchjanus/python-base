# search 01.py
import re

pattern = 'cat'

text = """I once had a big fat cat
    Who caught a big friendly rat.
    She played with it like a toy
    It gave her so much joy
    That she spared it and that was that.
    """

match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))

# group()- Вернуть строку, где было совпадение с регулярным выражением
print(match.group())

# start() - Вернуть позицию начала совпадения
# end()- Вернуть позицию конца совпадения
# метод search() сканирует всю строку: для него начало не обязательно в нуле:
print(match.start(),match.end())

# Выведем позицию (начальную и конечную) первого совпадения.
# span()- Вернуть кортеж (start, end) позиций совпадения
print(match.span())

# Выведем строку, переданную в функцию.
print(match.string)
