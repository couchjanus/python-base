# 05_create.py
import os
import sqlite3

db_filename = 'todo.db'

# Выполняем поиск файла базы данных перед его открытием с помощью connect()
db_is_new = not os.path.exists(db_filename)

# Открываем базу данных
conn = sqlite3.connect(db_filename)

# Запускаем скрипт дважды
# Скрипт создает пустой файл, если файл не существует.
if db_is_new:
    print('Need to create schema')
else:
    print('Database exists, assume schema does, too.')

# Закрьmаем базу данных
conn.close()
