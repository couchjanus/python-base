# 11_cursor_description.py
import sqlite3

db_filename = 'todo.db'

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()

    cursor.execute("""
    select * from task where project = 'pycat'
    """)

    print('Task table has these columns:')
    for colinfo in cursor.description:
        print(colinfo)
