"""
Database code for communicating with a sqlite database
"""
import logging
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
                """CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT, expiredate TEXT, details TEXT, priority INTEGER default 1, status TEXT default 'current', completed INTEGER default 0, project TEXT not null references projects(name))""")
            self.__cursor.execute("CREATE TABLE IF NOT EXISTS projects(name TEXT PRIMARY KEY, description TEXT, deadline TEXT)")
            self.__cursor.execute(f"INSERT INTO projects (name, description, deadline) VALUES('First', 'First Project Description', '2020/12/31')")
            self.__conn.commit()
        except:
            pass

    def get_all_projects(self):
        self.__cursor.execute("SELECT name FROM projects")
        temp_list = []
        for row in self.__cursor:
            temp_list.append(row[0])
        return tuple(temp_list)

    def get_all_tasks(self):
        """
        Returns all of tasks in the database
        """
        self.__cursor.execute("SELECT * FROM tasks")
        return self.__cursor.fetchall()

    def get_by_id(self, idtofind):
        """
        Returns a task by the given id
        """
        logging.debug(f"getting data by id: {idtofind}")
        self.__cursor.execute(f"SELECT name, expiredate, details, priority, status, project FROM tasks WHERE id='{idtofind}'")
        return self.__cursor.fetchone()

    def add_task(self, name, expiredate, details, priority, status, project):
        """
        Adds a new entry to the database
        """
        self.__cursor.execute(
            "INSERT INTO tasks(name, expiredate, details, priority, status, project) VALUES(?,?,?,?,?,?)", (name, expiredate, details, priority, status, project))
        self.__conn.commit()

    def add_project(self, name, description, deadline):
        try:
            self.__cursor.execute("INSERT INTO projects(name, description, deadline) VALUES(?,?,?)", (name, description, deadline))
            self.__conn.commit()
        except sql.IntegrityError:
            logging.debug("{name} project already exists so not going to add")

    def update_value(self, dataid, nameofvalue, thevalue):
        self.__cursor.execute(f"UPDATE tasks SET {nameofvalue}='{thevalue}' WHERE id='{dataid}'")
        self.__conn.commit()

    def reset(self):
        """
        Resets the database to default
        """
        self.__conn.execute("DELETE * FROM tasks")
        self.__conn.execute("DELETE FROM sqlite_sequence WHERE name='tasks'")

    def close(self):
        """
        Closes the database
        """
        self.__conn.close()
        logging.info("Database closed")
