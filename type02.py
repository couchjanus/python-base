#! /usr/bin/env python
# coding: utf

# Можно использовать двойные или одинарные кавычки:
print("foobar" == 'foobar')
# Для многострочных блоков текста используют тройные кавычки: """foo ... bar"""
# Подряд идущие строковые литералы “склеиваются”:
print("foo" "bar")

# Строки можно склеивать, даже если они записаны с разными кавычками.
print('Kings' + 'wood')      # => Kingswood
print('Kings' + 'road')      # => Kingsroad

# ошибка:
print("King's" + 'Landing')  # => King'sLanding
# King’s Landing нужно писать через пробел! 
# пробелы в самом коде слева и справа от символа + не имеют значения, потому что они не являются частью строк.

str1 = 'First line.\nSecond line.'  # \n means newline
print(str1)
print('C:\some\name')  # here \n means newline!

hello = "This is a rather long string containing\n\
several lines of text just as you would do in C.\n\
   Note that whitespace at the beginning of the line is\
significant."
print(hello)


print r'C:\some\name'  # note the r before the quote

hello = r"This is a rather long string containing\n\
several lines of text much as you would do in C."
print(hello)

s = ("Это отличный способ объединить две длинные строки, потому что он основан на конкатенации строковых литералов.")
print(s)

print("""
Usage: thingy [OPTIONS]
    -h                        Display this usage message
    -H hostname               Hostname to connect to
""")


# Строки чувствительны к регистру; 
Hello = "Hello"
hello = "hello"
# Строки Hello и hello содержат одинаковый набор символов, однако они не равны, поскольку одна из них содержит символы верхнего регистра. 
print("Hello == hello: ", Hello == hello) # Hello == hello:  False

Hello_there = "Hello"
print("Hello == Hello_there", Hello == Hello_there) # Hello == Hello_there:  True

# Также для сравнения строк можно использовать операторы > и <. Python выполнит лексикографическое сравнение строк на основе значений символов ASCII.

# такой ход в Python невозможен:
var = 3
var += "string2" # Порождается исключение TypeError: unsupported operand type(s) for +=: 'int' and 'str'
var = str(var)   # и потребуется явное преобразование типов
var += "string2" # теперь ОК
print(var) # Выведет "3string2"
