# 04_cursor.py
import sqlite3

# Получаем объект указателя на соединения. 
connection = sqlite3.connect('testdb.db')

# Создается курсор из соединения с БД:
cursor = connection.cursor()

# Закрьmаем базу данных
connection.close()
