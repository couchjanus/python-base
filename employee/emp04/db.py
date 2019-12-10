"""
Database code for communicating with a sqlite database
"""
import sqlite3 as sql

class Database:
    """
    The database handler where all the information will be saved to file
    """
    def __init__(self, filename):
        self.__filename = filename
        self.__conn = sql.connect(filename)
        self.__cursor = self.__conn.cursor()
        self.__create_database()

    def __create_database(self):
        """
        Creates the database if it does not exist
        """
        try:
            self.__cursor.execute(
                """CREATE TABLE IF NOT EXISTS employees(id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT, last_name TEXT)""")
            self.__conn.commit()
        except:
            pass

    def get_employees(self):
        self.__cursor.execute("SELECT * FROM employees")
        temp_list = []
        for row in self.__cursor:
            temp_list.append(row)
        return tuple(temp_list)


    def get_by_id(self, id):
        """
        Returns a employee by the given id
        """
        self.__cursor.execute(f"SELECT * FROM employees WHERE id='{id}'")
        return self.__cursor.fetchone()

    def add_employee(self, first_name, last_name):
        """
        Adds a new entry to the database
        """
        self.__cursor.execute(
            "INSERT INTO employees(first_name, last_name) VALUES(?,?)", (first_name, last_name))
        self.__conn.commit()

    def update_value(self, id, nameofvalue, thevalue):
        self.__cursor.execute(f"UPDATE employees SET {nameofvalue}='{thevalue}' WHERE id='{id}'")
        self.__conn.commit()

    def reset(self):
        """
        Resets the database to default
        """
        self.__conn.execute("DELETE * FROM employees")
        self.__conn.execute("DELETE FROM sqlite_sequence WHERE name='employees'")

    def close(self):
        """
        Closes the database
        """
        self.__conn.close()
