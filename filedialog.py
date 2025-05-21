import tkinter as tk
from tkinter import *
from tkinter import filedialog


mainwindow = tk.Tk()
mainwindow.title("File Dialog")

def btn_handler():
    file = filedialog.askopenfilenames(title='Select a text file', initialdir='.', filetypes=(('text files', '*.txt'),('PDF files', '*.pdf'), ('Python files', '.py'), ('All files', '*.*')))
    print('Selected file is/are : ', file)

btn = Button(mainwindow, text='Open', command=btn_handler)
btn.pack()


mainwindow.geometry("500x500")
mainwindow.mainloop()