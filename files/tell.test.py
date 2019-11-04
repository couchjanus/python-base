# -*- coding: utf-8 -*-
# tell.test.py

# метод tell() сообщает в скольких байтах от начала файла мы сейчас находимся.

my_file = open("some.txt")
my_file.read(10)
print ("Я на позиции:", my_file.tell())
my_file.close()
