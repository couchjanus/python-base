# 01.py
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
    print("match found")
    print(result)

# Искомая подстрока найдена. Результат:
# <re.Match object; span=(0, 1), match='I'>

# Анализ объекта
# dir возвращает список атрибутов и методов объекта:

print(dir(result)) # получим все методы объекта. 

# Функция type возвращает тип объекта:
print(type(result))

# id возвращает уникальный идентификатор объекта:
print(id(result))

# Модуль inspect

# Модуль inspect предоставляет несколько полезных функций для получения информации об объектах. Например, вы можете проверить члены объекта, запустив:

import inspect
print(inspect.getmembers(result))
