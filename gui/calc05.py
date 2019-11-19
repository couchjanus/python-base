from tkinter import *

# минимальное приложение на Tkinter:
root = Tk()
# За создание окна отвечает класс Tk(), и первым делом нужно создать экземпляр этого класса. Этот экземпляр принято называть root, хотя вы можете назвать его как угодно.

# title - заголовок окна
root.title("Simple calculator")

# geometry - устанавливает геометрию окна в формате ширинаxвысота+x+y (пример: geometry("600x400+40+80") - поместить окно в точку с координатам 40,80 и установить размер в 600x400). Размер или координаты могут быть опущены (geometry("600x400") - только изменить размер, geometry("+40+80") - только переместить окно)

root.geometry("600x200+40+80")

# root.minsize(600, 230)

# root.resizable(width=True, height=True)
root.resizable(width=False, height=False)

entry = Entry(width=30)
entry.grid(row=0,column=0,columnspan=6,pady=3)
Button(root, text="C", width = 10).grid(row=0, column = 3)
Button(root, text="C", width = 10).grid(row=0, column = 4)
bttn_list = (
"7", "8", "9", "/", "(",  ")",
"4", "5", "6", "*", "xⁿ", "√2",
"1", "2", "3", "-", "sin", "cos",
"0", ".", "±", "+", "n!", "π", 
 "=")

# Создаем кнопки для калькулятора:

r = 1
c = 0
for i in bttn_list:
    Button(root, text=i, width = 10).grid(row=r, column = c)
    c += 1
    if c > 5:
        c = 0
        r += 1

# В конце программы, нужно использовать функцию mainloop 
root.mainloop()
