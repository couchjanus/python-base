# 01_sqlight.py
import sqlite3

print(sqlite3.version)
# '2.6.0' - это версия pysqlite

# Получаем номер спецификации

# Получить номер версии используемого модуля sqliteЗ можно с помощью атрибутов sqlite_version и sqlite_version_info.

# Атрибут sqlite_version возвращает номер версии в виде строки
print(sqlite3.sqlite_version)

#  Атрибут sqlite_version_info- в виде кортежа из трех или четырех чисел.
print(sqliteЗ.sqlite_version_info)
