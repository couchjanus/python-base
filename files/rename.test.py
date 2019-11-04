# -*- coding: utf-8 -*-
# rename.test.py


# Для переименования вызывается функция rename(source, target), 
# первый параметр которой - путь к исходному файлу, 
# а второй - новое имя файла. 
# В качестве путей могут использоваться как абсолютные, 
# так и относительные. 
# Например, пусть в папке C://SomeDir/ располагается файл somefile.txt. 
# Переименуем его в файл "hello.txt":

import os
 
os.rename("C://SomeDir/somefile.txt", "C://SomeDir/hello.txt")


