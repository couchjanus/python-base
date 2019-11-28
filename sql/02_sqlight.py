# 02_sqlight.py
# Подключаем модуль sqlite3
import sqlite3

# Открываем базу данных
con = sqlite3.connect("testdb.db")

# Работаем с базой данных

# Закрьmаем базу данных
con.close()