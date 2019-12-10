from tkinter import *

class Widget():

    def __init__(self):
        
        self.__button_font = ('Verdana', 14)
        self.__entry_font = ('Verdana', 16)
        self.__button_width = 12
        self.__button_height = 1

    def button(self, title, x, y, px, py, bg, fg, cs, cmd):
        self.__b = Button(
            self, text=title, width=self.__button_width,
            height=self.__button_height, font=self.__entry_font, background=bg,foreground=fg, command=cmd)
        self.__b.grid(row=x, column=y, padx=px, pady=py, columnspan=cs)

    def entry(self, x, y, py):
        self.__e = Entry(self, font=('Verdana', 16))
        self.__e.grid(row=x, column=y, pady=py)
        
    def label(self, txt, x, y, bg, px, py, cs):
        self.__l = Label(self, text = txt, bg=bg, font=('Verdana', 16))
        self.__l.grid(row=x, column=y, padx=px, pady=py, columnspan=cs)

    def get_fnt(self):
        """Вернуть font."""
        return self._fnt

    def set_fnt(self, fnt):
        """Установить font в значение 'fnt'."""
        self._fnt = fnt
