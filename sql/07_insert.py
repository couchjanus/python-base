# 07_insert.py
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
        
        print('Inserting initial data')

        conn.executescript("""
        insert into project (name, description, deadline)
        values ('pycat', 'Python Cat of the Week',
                '2019-11-28');

        insert into task (details, status, deadline, project)
        values ('write about select cat', 'done', '2019-12-25',
                'pycat');

        insert into task (details, status, deadline, project)
        values ('write about random cat', 'waiting', '2019-12-22',
                'pycat');

        insert into task (details, status, deadline, project)
        values ('write about black cat', 'active', '2019-12-31',
                'pycat');
        """)

    else:
        print('Database exists, assume schema does, too.')
