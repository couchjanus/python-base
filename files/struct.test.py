# -*- coding: utf-8 -*-
# struct.test.py

# В следующем примере мы упаковываем в структуру два числа
#  – целое и float, строку из пяти символов, 
# сохраняем в бинарный файл, а потом извлекаем из файла:

from struct import *

out = open("123.bin", "wb")    

format = "if5s"             
data = pack(format, 24, 12.48, bytes("12345", 'utf-8'))

out.write(data)
out.close()

input = open("123.bin", "rb")
data = input.read()
input.close()
format = "if5s"                   # one integer

value,value2,value3 = unpack(format, data) # note the ',' in 'value,': 
# unpack apparently returns a n-uple
print(value)
print(value2)
print(value3)
print(calcsize)

