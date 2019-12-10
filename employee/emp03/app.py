from tkinter import *
from tkinter import ttk, messagebox

from .addedit import AddEditWindow
from .widgets import Widget

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


class App(Tk, Widget):

    def __init__(self, **kwargs):
        super(App, self).__init__(**kwargs)
    
        self.title('Employee')
        self.protocol('WM_DELETE_WINDOW', self.destroy_app)
        self.employeelist = EmployeeList(self)
        self.employeelist.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        Widget.__init__(self)
        self.fnt = ('Verdana', 16)

        self.button('Add Employee', 2, 0, 0, 10, '#5c4fa1', "white", 1, self.create)
        self.button('Exit', 2, 1, 0, 10, '#c54f1a', "white", 1, self.destroy_app)
    
    def create(self):
        popup = AddEditWindow()
        self.wait_window(popup)
 
    def destroy_app(self):
        """ Exit from app """
        self.destroy()
