import tkinter as tk
from tkinter import *

mainwindow = tk.Tk()
mainwindow.title("Menu Example")

mn = Menu(mainwindow)

def open_handler():
    my_str.set('open file is called')

def save_handler():
    my_str.set('save file is called')
    
filemenu = Menu(mn, tearoff=0)
filemenu.add_command(label="Open", command=open_handler)
filemenu.add_command(label="Save", command=save_handler)
filemenu.add_command(label="Save As...")
filemenu.add_separator()
filemenu.add_checkbutton(label="Saved")
filemenu.add_checkbutton(label="Other")

editmenu = Menu(mn, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")
editmenu.add_separator()
editmenu.add_radiobutton(label="text")
editmenu.add_radiobutton(label="pdf")

mn.add_cascade(label="File", menu=filemenu)
mn.add_cascade(label="Edit", menu=editmenu)

my_str = StringVar()
lbl = Label(mainwindow, textvariable=my_str, font=(None, 26))
lbl.pack()

mainwindow.config(menu=mn)

mainwindow.geometry('400x400')
mainwindow.mainloop()