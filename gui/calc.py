from tkinter import *
from tkinter import messagebox
import math

class Calc:
    def __init__(self, master):
        """Constructor method"""
        master.title('Simple calculator')
        master.geometry()
        self.e = Entry(master, width = 30, font='Arial 14')
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set() # Sets focus on the input text area
        Button(master, text='c', font='Arial 14', width = 10, command=lambda : self.clear()).grid(row=0, column = 3)
        Button(master, text='CA', font='Arial 14', width = 10, command=lambda: self.clearall()).grid(row=0, column = 4)

        # создаём виджет
        self.closeButton = Button(master, text='Exit', font='Arial 14', width = 10, command = lambda:master.quit())
        self.closeButton.grid(row=5, column = 1)
        master.protocol('WM_DELETE_WINDOW', self.destroyApp(master)) # обработчик закрытия окна

        bttn_list = (
        "7", "8", "9", "/", "(",  ")",
        "4", "5", "6", "*", "xⁿ", "√2",
        "1", "2", "3", "-", "sin", "cos",
        "0", ".", "±", "+", "n!", "π", 
        )

        self.ops = "-+0123456789.*/)("

        # Создаем кнопки для калькулятора:

        r = 1
        c = 0
        for i in bttn_list:
            if i in self.ops:
                cmd=lambda x=i: self.action(x)
            elif i == "±":
                cmd=lambda: self.sign()
            elif i == "π":
                cmd=lambda: self.pi()
            elif i == "sin":
                cmd=lambda: self.sin()
            elif i == "cos":
                cmd=lambda: self.cos()
            elif i == "xⁿ":
                cmd=lambda x="**": self.action(x)
            elif i == "n!":
                cmd=lambda: self.factor()
            elif i == "√2":
                cmd=lambda: self.sqrt()

            Button(master, text=i, font='Arial 14', command = cmd, width = 10).grid(row=r, column = c)
            c += 1
            if c > 5:
                c = 0
                r += 1
        
        Button(master, text='=', font='Arial 14', width = 10, command=lambda:self.equals()).grid(row=5, column = 0)
    
    def action(self, val):
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END, val)
    
    def clearall(self):
        """when clear button is pressed,clears the text input area"""
        self.e.delete(0,END)

    def clear(self):
        val=self.e.get()[:-1]
        self.patch(val)

    def patch(self, val):
        self.e.delete(0, END)
        self.e.insert(0, val)

    def equals(self):
        """when the equal button is pressed"""

        self.expression = self.e.get()
        
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
            if self.e.get()[0] == "-":
                self.e.delete(0)
            else:
                self.e.insert(0, "-")
        except IndexError:
            pass
    
    def pi(self):
        v = math.pi
        self.patch(v)

    def sin(self):
        v = math.sin(float(self.e.get()))
        self.patch(v)

    def cos(self):
        v = math.cos(float(self.e.get()))
        self.patch(v)

    def factor(self):
        v = math.factorial(int(float(self.e.get())))
        self.patch(v)

    def sqrt(self):
        v = math.sqrt(float(self.e.get()))
        self.patch(v)

    def destroyApp(self, master):
        master.quit() # явное указание на выход из программы

# Main
if __name__ == '__main__':
    root = Tk()
    obj=Calc(root) # object instantiated
    root.mainloop()
