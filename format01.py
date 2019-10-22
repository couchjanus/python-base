#! /usr/bin/env python
# coding: utf

# Метод str.format(...) Возвращает копию строки str, отформатированную в соответствии с заданными аргументами.
print("{}, {}, how are you?".format("Hello", "Sally"))
print("Today is October, {}th.".format(22))
# {} обозначает место, в которое будет подставлен позиционный аргумент.

# Внутри {} можно опционально указать способ преобразования объекта в строку и спецификацию формата.
# Для преобразования объекта в строку используются первые буквы соответствующих функций:

print("{!s}".format("я строка")) # str
print("{!r}".format("я строка")) # repr
print("{!a}".format("я строка")) # ascii
print("'\\u044f \\u0441\\u0442\\u0440\\u043e\\u043a\\u0430'")

print('{0}, {1}, {2}'.format('a', 'b', 'c')) # 'a, b, c'
print('{}, {}, {}'.format('a', 'b', 'c')) # 'a, b, c'
print('{2}, {1}, {0}'.format('a', 'b', 'c')) # 'c, b, a'
print('{2}, {1}, {0}'.format(*'abc')) # 'c, b, a'
print('{0}{1}{0}'.format('abra', 'cad')) # 'abracadabra'
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')) # 'Coordinates: 37.24N, -115.81W'
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord)) #'Coordinates: 37.24N, -115.81W'
