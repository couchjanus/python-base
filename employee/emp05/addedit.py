"""
Template classes for adding and editing the Employee items
"""

from tkinter import Toplevel, StringVar, Label, Frame, OptionMenu, Button, IntVar, Entry, messagebox
from .widgets import Widget

class AddEditEntry(Frame, Widget):
    """
    Template widget for adding/editing the entry
    """
    def __init__(self, parent):
        Frame.__init__(self, parent, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=100, height=100, borderwidth = 2)

        self.__f_name_var = StringVar(self)
        self.__l_name_var = StringVar(self)
        
        Widget.__init__(parent)
        
        self.fnt = ('Verdana', 16)
        
        self.grid(padx=20, pady=20)
        self.label('Employee Management System', 0, 0, "white", 15, 15, 4)
        self.label('First Name : ', 1, 0, "white", 1, 5, 1)
        self.__f_name = self.entry(1, 1, 5, self.__f_name_var)
        self.label('Last Name  : ', 2, 0, "white", 1, 5, 1)
        self.__l_name = self.entry(2, 1, 5, self.__l_name_var)
       

    def get_values(self):
        datatoreturn = (
            self.__f_name_var.get(),
            self.__l_name_var.get(),
            )
        return datatoreturn

    def set_values(self, fname, lname):
        self.__f_name_var.set(fname)
        self.__l_name_var.set(lname)
        

class AddEditWindow(Toplevel, Widget):

    def __init__(self):
        Toplevel.__init__(self)
        Widget.__init__(self)
        self.fnt = ('Verdana', 16)

        self.wm_title("Add Employee")
        self.__the_entry = AddEditEntry(self)
        self.__the_entry.grid(row=0, column=0,columnspan=3, pady=10)

        self.button('Save', 3, 0, 0, 10, '#a15c4f', "white", 2, self.__save)
        self.button('Close', 3, 1, 0, 10, '#5c4fa1', "white", 2, self.__closeWindow)


    def __closeWindow(self):
        self.destroy()

    def get_data(self):
        return self.__the_entry.get_values()

    def __save(self):
        self.destroy()

