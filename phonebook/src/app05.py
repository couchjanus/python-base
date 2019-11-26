from tkinter import *
from .contact import Contact
from .phonebook01 import Phonebook

class App:
    def __init__(self, master):
        """Constructor method"""
        
        self.container = master
        self.container.title('Phonebook')
        self.container.geometry()
        
        self.phonebook = Phonebook("phonebook.data")
        
        self.button_font = ('Verdana', 14)
        self.entry_font = ('Verdana', 16)
        self.button_width = 12
        self.button_height = 1
        
        self.label('Name', 0, 0)
        self.label('Phone', 0, 2)
        self.label('Mobile', 1, 0)
        self.label('Address', 1, 2)
       
        self.e_name = self.entry(0, 1)
        self.e_phone = self.entry(0, 3)
        self.e_mobile = self.entry(1, 1)
        self.e_addr = self.entry(1, 3)
        
        self.button('View all', 2, 3, self.view_command)
        self.button('Search entry', 3, 3, self.search_command)
        self.button('Add entry', 4, 3, self.add_command)
        self.button('Update selected', 5, 3, self.update_command)
        self.button('Delete selected', 6, 3, self.delete_command)
        self.button('Exit', 7, 3, self.destroy_app)

        self.container.protocol('WM_DELETE_WINDOW', self.destroy_app())

        self.li = self.list(10, 50, 2, 0, 6, 2, self.get_selected_row)
        self.sb = self.scrollbar(2, 2, 6)
        
        self.li.config(yscrollcommand = self.sb.set)
        self.sb.config(command = self.li.yview)

    def entry(self, x, y):
        e = Entry(self.container, font=self.entry_font)
        e.grid(row=x, column=y)
        return e

    def label(self, txt, x, y):
        self.l = Label(self.container, text = txt)
        self.l.grid(row=x, column=y)

    def button(self, title, x, y, cmd):
        self.b = Button(
            self.container, text=title, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=cmd)
        self.b.grid(row=x, column=y)

    def list(self, h, w, x, y, rs, cs, cmd):
        li = Listbox(self.container, height = h, width = w)
        li.grid(row=x, column=y, rowspan = rs, columnspan = cs)
        li.bind('<<ListboxSelect>>', cmd)
        return li

    def scrollbar(self, x, y, rs):
        sb = Scrollbar(self.container)
        sb.grid(row=x, column=y, rowspan = rs)
        return sb

    def destroy_app(self):
        """ Exit from app """
        self.container.quit() 

    def search_command(self):
        pass

    def view_command(self):
        self.li.delete(0, END)
        for row in self.phonebook.view():
            self.li.insert(END, (row.name, row.phone, row.mobile, row.address))

    def add_command(self):
        contact = Contact(self.e_name.get(), self.e_phone.get(), self.e_mobile.get(), self.e_addr.get())
        self.phonebook.save(contact)
        self.e_name.delete(0, END)
        self.e_phone.delete(0, END)
        self.e_mobile.delete(0, END)
        self.e_addr.delete(0, END)

    def update_command(self):
        pass

    def delete_command(self):
        pass

    def get_selected_row(self):
        pass

    def get_selected_row(self,event):
        try:
            index = self.li.curselection()[0]
            self.selected_tuple = self.li.get(index)
            print(self.selected_tuple)
            self.e_name.delete(0,END)
            self.e_name.insert(END,self.selected_tuple[0])
            self.e_phone.delete(0, END)
            self.e_phone.insert(END,self.selected_tuple[1])
            self.e_mobile.delete(0, END)
            self.e_mobile.insert(END,self.selected_tuple[2])
            self.e_addr.delete(0, END)
            self.e_addr.insert(END,self.selected_tuple[3])
        except IndexError:
            pass
