# 06_create_schema.py
import os
import sqlite3

db_filename = 'todo.db'
schema_filename = 'todo_schema.sql'

# Выполняем поиск файла базы данных перед его открытием с помощью connect()
db_is_new = not os.path.exists(db_filename)

# Скрипт создает пустой файл, если файл не существует.
with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Schema Created Successfully')

    else:
        print('Database exists, assume schema does, too.')
