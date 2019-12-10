# from tkinter import *
from tkinter import Toplevel, StringVar, Label, Frame, OptionMenu, Button, IntVar, Entry, messagebox

class Widget():

    def __init__(self):
        
        self.__button_width = 12
        self.__button_height = 1

    @property
    def fnt(self):
        # Определение свойства 'fnt': возвращает 'self._fnt' и позволяет работать с
        # font извне, как с обычным атрибутом
        return self._fnt

    @fnt.setter
    def fnt(self, fnt):
        """Установить font в 'fnt'.
        Метод может быть опущен, свойство 'fnt' долно быть доступно только для чтения.
        """
        self._fnt = fnt

    def button(self, title, x, y, px, py, bg, fg, cs, cmd):
        self.__b = Button(
            self, text=title, width=12,
            height=1, font=self.fnt, background=bg,foreground = fg, command=cmd)
        self.__b.grid(row=x, column=y, padx=px, pady=py, columnspan=cs)

    def entry(self, x, y, py, tv):
        self.__e = Entry(self, font=self.fnt, textvariable=tv)
        self.__e.grid(row=x, column=y, pady=py)
        
    def label(self, txt, x, y, bg, px, py, cs):
        self.__l = Label(self, text = txt, bg=bg, font=self.fnt)
        self.__l.grid(row=x, column=y, padx=px, pady=py, columnspan=cs)
