from tkinter import *
from tkinter import ttk, messagebox
import logging
from .db import Database

class TodoList(ttk.Treeview):
    """
    The list box that is used to hold the data
    """

    def __init__(self, parent):
        cols = ("ID", "Name", "Due Date")
        self.__curr_index = 0
        ttk.Treeview.__init__(self, parent, columns=cols, show="headings")

        for eachcol in cols:
            self.heading(column=eachcol, text=eachcol)
            self.column(column=eachcol, width=100, minwidth=0)

    def load_data(self, rowsToLoad):
        """
        Adds row into the treeview
        """
        self.delete(*self.get_children())
        for item in rowsToLoad:
            self.insert("", self.__curr_index, text=item[0], values=item)
            self.__curr_index += 1

class App(Tk):
    """
    The main tktiner app window
    """
    def __init__(self, filename):
        """
        Constructor method
        requires filename/path of the database
        """
        Tk.__init__(self)
       
        self.title('Todos')
        self.protocol('WM_DELETE_WINDOW', self.destroy_app)

        self.geometry()
        self.button_font = ('Verdana', 14)
        self.entry_font = ('Verdana', 16)
        self.button_width = 12
        self.button_height = 1

        self.__database = Database(filename)

        self.todolist = TodoList(self)
        self.todolist.load_data(self.__database.get_all_tasks())

        self.todolist.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        
        self.button('Add project', 2, 0, self.add_project)
        self.button('Add task', 2, 1, self.add_task)
        self.button('Exit', 2, 2, self.destroy_app)


    def button(self, title, x, y, cmd):
        self.b = Button(
            self, text=title, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=cmd)
        self.b.grid(row=x, column=y)

    def destroy_app(self):
        """ Exit from app """

        logging.debug("Quiting app!")
        self.destroy()

    def add_project(self):
        pass

    def add_task(self):
        pass
