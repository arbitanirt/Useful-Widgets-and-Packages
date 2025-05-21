import tkinter as tk
from tkinter import ttk, Label, Frame, Button

mainwindow = tk.Tk()
mainwindow.title('Tab for an Application')

tab = ttk.Notebook(mainwindow, height=350, width=350)

#l1 = Label(tab, text="this is Tab 1", bg='blue')
#l2 = Label(tab, text="this is Tab 2", bg='green')
#l3 = Label(tab, text="this is Tab 3", bg='red')
#l4 = Label(tab, text="this is Tab 4", bg='orange')

#tab.add(l1, text="Onglet 1")
#tab.add(l2, text="Onglet 2")
#tab.add(l3, text="Onglet 3")
#tab.add(l4, text="Onglet 4")

fm1 = Frame(tab)

lb1 = Label(fm1, text='Label1', bg='blue').pack()
btn1 = Button(fm1, text='Click Me', bg='orange').pack()

fm2 = Frame(tab)

lb2 = Label(fm2, text='Label2', bg='green', width=20, height=10).pack()
btn2 = Button(fm2, text='Click Me', bg='red').pack()


tab.add(fm1, text="Frame 1")
tab.add(fm2, text="Frame 2")



tab.pack()


mainwindow.geometry('400x400')
mainwindow.mainloop()