# -*- coding: utf-8 -*-
# shelve.close.file.test.py

import shelve
# Для открытия файла модуль shelve использует функцию open():
d = shelve.open('simlefile.txt')

# Для закрытия подключения к файлу вызывается метод close():
d.close()

