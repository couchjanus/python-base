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
        self.__status_selected.set(status)
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

class AddProject(Toplevel):
    """
    tkinter popup window to add a project
    """
    def __init__(self, projects):
        self.__entry_formated = None
        self.__description_formated = None
        self.__deadline_formated = None
        
        self.__projects = projects
        Toplevel.__init__(self)
        self.wm_title("Add Project")
        self.__entry = Entry(self)
        self.__description = Entry(self)
        self.__deadline = Entry(self)
        
        self.__confirm = Button(self, text="Confirm", command=self.confirm)
        self.__entry.pack()
        self.__description.pack()
        self.__deadline.pack()
        self.__confirm.pack()
        self.protocol("WM_DELETE_WINDOW", self.close)

    def close(self):
        """
        Allows the user to choose whether to save or not when clicking the close button
        """
        if self.__entry.get() == "":
            self.destroy()
        else:
            dialog = messagebox.askyesnocancel("Leave without saving","Do you want to save before leaving?")
            if dialog:
                logging.debug("user wants to save before leaving")
                if self.confirm() != None:
                    self.confirm()
            elif dialog == None:
                logging.debug("User wants to stay")
            else:
                logging.debug("User wants to leave without saving")
                self.destroy()

    def get_data(self):
        """
        Returns the user data
        """
        return self.__entry_formated, self.__description_formated, self.__deadline_formated

    def confirm(self):
        """
        gets the user entry and compares it to the ones given
        if it is present in the ones given displays error message
        """
        if self.__entry.get().capitalize() not in self.__projects:
            self.__entry_formated = self.__entry.get().capitalize()
            self.__description_formated = self.__description.get() 
            self.__deadline_formated = self.__deadline.get()
            self.destroy()
        else:
            logging.error("Project already exists")
            messagebox.showerror("Already exists", "The project you chose already exists!")
