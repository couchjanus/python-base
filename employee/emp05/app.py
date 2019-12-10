from tkinter import *
from tkinter import ttk, messagebox

from .addedit import AddEditWindow
from .widgets import Widget
from .db import Database
import logging

class EmployeeList(ttk.Treeview):
    """
    The list box that is used to hold the data
    """
    def __init__(self, parent):
        cols = ("ID", "Name", "Job Title")
        self.__curr_index = 0
        ttk.Treeview.__init__(self, parent, columns=cols, show="headings")

        for eachcol in cols:
            self.heading(column=eachcol, text=eachcol)
            self.column(column=eachcol, width=100, minwidth=0)
    
    def load_data(self, rows):
        """
        Adds row into the treeview
        """
        self.delete(*self.get_children())
        for item in rows:
            self.insert("", self.__curr_index,  values=item)
            self.__curr_index += 1

# 
class App(Tk, Widget):

    def __init__(self):
        super(App, self).__init__()
    
        self.title('Employee')
        self.protocol('WM_DELETE_WINDOW', self.destroy_app)
        self.employeelist = EmployeeList(self)
        
        self.__database = Database('employees.db')
        
        self.__database.init_db()

        print(self.__database.get_employees())

        self.employeelist.load_data(self.__database.get_employees())
        self.employeelist.bind("<<TreeviewSelect>>", self.edit)
        self.employeelist.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        Widget.__init__(self)
        self.fnt = ('Verdana', 16)

        self.button('Add Employee', 2, 0, 0, 10, '#5c4fa1', "white", 1, self.create)
        self.button('Exit', 2, 1, 0, 10, '#c54f1a', "white", 1, self.destroy_app)
    
    def create(self):
        popup = AddEditWindow()
        self.wait_window(popup)
        first_name, last_name = popup.get_data()
        if first_name != "":
            self.__database.add_employee(first_name, last_name)
            self.employeelist.load_data(self.__database.get_employees())
        else:
            logging.warning("No data was given")

    def edit(self):
        pass
 
    def destroy_app(self):
        """ Exit from app """
        self.destroy()
