from tkinter import *
from tkinter import messagebox
import math

class Calc:
    def __init__(self, master):
        """Constructor method"""
        
        self.container = master
        
        self.container.title('Simple calculator')
        self.container.geometry()
        
        self.button_font = ('Verdana', 15)
        self.entry_font = ('Verdana', 20)
        self.button_width = 4
        self.button_height = 1
        self.ops = "-+0123456789.*/)("
        self.button_list = (
                "7", "8", "9", "/", "(",  ")",
                "4", "5", "6", "*", "xⁿ", "√2",
                "1", "2", "3", "-", "sin", "cos",
                "0", ".", "±", "+", "n!", "π", 
        )

        self.string = ''
        self.entry(0, 0)
        self.buttons()
        self.button_rem('<', 0, 3)
        self.button_clear('CA', 0, 4)
        self.button_eq('=', 5, 1)
        

    def entry(self, x, y):
        self.entry = Entry(self.container, font=self.entry_font, width=self.button_width*5)
        self.entry.grid(row=x, column=y, columnspan=4, sticky='we')
        self.entry.focus_set()

    def button(self, char, x, y):
        if char in self.ops:
            cmd=lambda : self.action(char)
        elif char == "±":
            cmd=lambda: self.sign()
        elif char == "π":
            cmd=lambda: self.pi()
        elif char == "sin":
            cmd=lambda: self.sin()
        elif char == "cos":
            cmd=lambda: self.cos()
        elif char == "xⁿ":
            cmd=lambda x="**": self.action(x)
        elif char == "n!":
            cmd=lambda: self.factor()
        elif char == "√2":
            cmd=lambda: self.sqrt()

        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=cmd)
        self.b.grid(row=x, column=y)

    def buttons(self):
        r = 1
        c = 0
        for i in self.button_list:
            self.button(i, r, c)
            c += 1
            if c > 5:
                c = 0
                r += 1
    
    def button_rem(self, char, x, y):
        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.clear)
        self.b.grid(row=x, column=y)
        
    def button_clear(self, char, x, y):
        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.clearall)
        self.b.grid(row=x, column=y)

    def button_eq(self, char, x, y):
        self.b = Button(
            self.container, text=char, width=self.button_width,
            height=self.button_height, font=self.entry_font,
            command=self.equal)
        self.b.grid(row=x, column=y, sticky='we', columnspan=2)
        
        # создаём виджет
        # self.closeButton = Button(master, text='Exit', font='Arial 14', width = 10, command = lambda:master.quit())
        # self.closeButton.grid(row=5, column = 1)
        # master.protocol('WM_DELETE_WINDOW', self.destroyApp(master)) # обработчик закрытия окна
        
    def action(self, val):
        self.entry.insert(END, val)
    
    def clearall(self):
        self.entry.delete(0,END)

    def clear(self):
        val=self.entry.get()[:-1]
        self.patch(val)

    def patch(self, val):
        self.entry.delete(0, END)
        self.entry.insert(0, val)

    def change_sign(self, char):
        self.entry.delete(0, END)
        self.entry.insert(0, val)

    def equal(self):
        self.expression = self.entry.get()
        
        if self.expression[0] not in self.ops:
            self.patch("First symbol is not number!")
            messagebox.showerror("Error!", "You did not enter the number!")

        try:
            self.value= eval(self.expression) #evaluate the expression using the eval function
        except SyntaxError or NameErrror:
            self.patch('Invalid Input!')
        else:
            self.patch(self.value)

    def sign(self):
        try:
            if self.entry.get()[0] == "-":
                self.entry.delete(0)
            else:
                self.entry.insert(0, "-")
        except IndexError:
            pass
    
    def pi(self):
        v = math.pi
        self.patch(v)

    def sin(self):
        v = math.sin(float(self.entry.get()))
        self.patch(v)

    def cos(self):
        v = math.cos(float(self.entry.get()))
        self.patch(v)

    def factor(self):
        v = math.factorial(int(float(self.entry.get())))
        self.patch(v)

    def sqrt(self):
        v = math.sqrt(float(self.entry.get()))
        self.patch(v)

    def destroyApp(self, master):
        master.quit() # явное указание на выход из программы

# Main
if __name__ == '__main__':
    root = Tk()
    obj=Calc(root) # object instantiated
    root.mainloop()
