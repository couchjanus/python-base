# 03_sqlight.py
# Подключаем модуль sqlite3
import sqlite3

# Доступ к базе, хранящейся: в файле c:\book\testdb.db

# con = sqlite3.connect(r"file:///c:/book/testdb.db", uri = True)
con = sqlite3.connect(r"file:////home/janus/www/python-base/sql/testdb.db?mode=rwc", uri = True)

# Закрьmаем базу данных
con.close()

# Доступ только для чтения
# con = sqlite3.connect(r"file:///c:/book/testdb.db?mode = ro", uri =True)
con = sqlite3.connect(r"file:////home/janus/www/python-base/sql/testdb.db?mode=ro", uri = True)
# Закрьmаем базу данных
con.close()
# Доступ к неизменяемой базе данных
# con = sqlite3.connect(r"file:///f:/testdb.db?immutable=1", uri = True)
con = sqlite3.connect(r"file:////home/janus/www/python-base/sql/testdb.db?immutable=1", uri = True)
con.close()
