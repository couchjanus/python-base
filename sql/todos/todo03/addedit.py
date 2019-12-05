"""
Template classes for adding and editing the database items
"""
import logging
from tkinter import Toplevel, StringVar, Label, Frame, OptionMenu, Button, IntVar, Entry, messagebox

class AddEditEntry(Frame):
    """
    Template widget for adding/editing the entry
    """
    def __init__(self, parent, possibleprojects):
        Frame.__init__(self, parent)
        self.__months = ("January", "February", "March", "April", "May",
                         "June", "July", "August", "September", "October",
                         "November", "December")
        self.__status = ("current", "mandatry", "stoped", "sheduker")
        self.__month_selected = StringVar(self, value=self.__months[0])
        self.__project_selected = StringVar(self, value="First")
        self.__status_selected = StringVar(self, value="current")
        
        self.__name_var = StringVar(self)
        self.__day_var = IntVar(self, value=1)
        self.__year_var = IntVar(self, value=2000)
        self.__details_var = StringVar(self)
        self.__priority_var  = IntVar(self, value=1)
        
        l_name = Label(self, text="Name:")
        self.__e_name = Entry(self, textvariable=self.__name_var)
        
        l_day = Label(self, text="Day:")
        self.__e_day = Entry(self, textvariable=self.__day_var)
        
        l_month = Label(self, text="Month:")
        self.__om_month = OptionMenu(self, self.__month_selected,
                                        *self.__months)
        l_year = Label(self, text="Year:")
        self.__e_year = Entry(self, textvariable=self.__year_var)
        
        l_details = Label(self, text="Description")
        self.__t_details = Entry(self, textvariable=self.__details_var)
        
        l_priority = Label(self, text="Priority")
        self.__e_priority = Entry(self, textvariable=self.__priority_var)
        
        l_status = Label(self, text="Status:")
        self.__om_status = OptionMenu(self, self.__status_selected,
                                        *self.__status)
        
        l_project = Label(self, text="Project")
        self.__om_project = OptionMenu(self, self.__project_selected, *possibleprojects)

        l_name.grid(row=0, column=0)
        self.__e_name.grid(row=0, column=1)

        l_day.grid(row=1, column=0)
        self.__e_day.grid(row=1, column=1)

        l_month.grid(row=2, column=0)
        self.__om_month.grid(row=2, column=1)

        l_year.grid(row=3, column=0)
        self.__e_year.grid(row=3, column=1)

        l_details.grid(row=4, column=0)
        self.__t_details.grid(row=4, column=1)
     
        l_status.grid(row=5, column=0)
        self.__om_status.grid(row=5, column=1)
        
        l_priority.grid(row=6, column=0)
        self.__e_priority.grid(row=6, column=1)

        l_project.grid(row=7, column=0)
        self.__om_project.grid(row=7, column=1)

    def set_values(self, day, monthint, year, name, details, priority, status, project):
        """
        Sets the values of the
        entries with the data given"
        """
        # makes it so that the value of the month list matches with the month number
        monthint -= 1
        self.__name_var.set(name)
        self.__day_var.set(day)
        self.__month_selected.set(self.__months[monthint])
        self.__year_var.set(year)
        self.__details_var.set(details)
        self.__priority_var.set(priority)
        self.__status_var.set(status)
        self.__project_selected.set(project)

    def get_values(self):
        """
        Returns pre-formated values
        """
        month = self.__months.index(self.__month_selected.get()) + 1
        date = f"{self.__day_var.get()}.{month}.{self.__year_var.get()}"
        datatoreturn = (
            self.__name_var.get(),
            date,
            self.__details_var.get(),
            self.__project_selected.get(),
            self.__status_selected.get(),
            self.__priority_var.get()
            )
        return datatoreturn

class AddEditWindow(Toplevel):
    """
    tkinter add/edit menu popup
    """

    def __init__(self, possibleprojects):
        Toplevel.__init__(self)
        self.wm_title("Add Task")
        self.__the_entry = AddEditEntry(self, possibleprojects)
        self.__b_ok = Button(self, text="Save", command=self.__closeWindow)
        self.__the_entry.pack()
        self.__b_ok.pack()

    def __closeWindow(self):
        """
        Closes the window
        """
        self.destroy()

    def get_data(self):
        """
        Returns TUPLE of (name, priority, date(d,M,yyyy), details,  status, project)
        """
        return self.__the_entry.get_values()
    
    def load_data(self, day, monthint, year, name, details, priority, status, project):
        self.wm_title("Edit Entry")
        logging.debug(f"Loading data: {day, monthint, year, name, details, project}")
        self.__the_entry.set_values(day, monthint, year, name, details, priority, status, project)
