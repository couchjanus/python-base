from tkinter import *

class Calc:
    def __init__(self, master):
        """Constructor method"""
        master.title('Simple calculator')
        master.geometry()
        self.e = Entry(master, width = 30, font='Arial 14')
        self.e.grid(row=0, column=0, columnspan=6, pady=3)
        self.e.focus_set() # Sets focus on the input text area
        Button(master, text='c', font='Arial 14', width = 10).grid(row=0, column = 3)
        Button(master, text='CA', font='Arial 14', width = 10).grid(row=0, column = 4)

        bttn_list = (
        "7", "8", "9", "/", "(",  ")",
        "4", "5", "6", "*", "xⁿ", "√2",
        "1", "2", "3", "-", "sin", "cos",
        "0", ".", "±", "+", "n!", "π", 
        )

        # Создаем кнопки для калькулятора:

        r = 1
        c = 0
        for i in bttn_list:
            cmd=lambda x=i: self.action(x)
            Button(master, text=i, font='Arial 14', command = cmd, width = 10).grid(row=r, column = c)
            c += 1
            if c > 5:
                c = 0
                r += 1
        
        Button(master, text='=', font='Arial 14', width = 10).grid(row=5, column = 0)
    
    def action(self, val):
        """pressed button's value is inserted into the end of the text area"""
        self.e.insert(END, val)

# Main
root = Tk()
obj=Calc(root) # object instantiated
root.mainloop()