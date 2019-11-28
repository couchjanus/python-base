# 16_argument_delete.py
import sqlite3
import sys

db_filename = 'todo.db'
id = int(sys.argv[1])

with sqlite3.connect(db_filename) as conn:
    cursor = conn.cursor()
    query = "DELETE FROM task WHERE id = :id"
    cursor.execute(query, {'id': id})
