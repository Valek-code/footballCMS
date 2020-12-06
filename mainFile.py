from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import csv
from komponente import timovi, igraci, treneri, sesije, sudac, selekcije


root = Tk()
root.title("Baze podataka - Projekt")
root.geometry("500x500")


# NOTEBOOK
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

# FRAMEOVI ( TABOVI )
frame = Frame(my_notebook, width=500, height=500, bg="white")
frame2 = Frame(my_notebook, width=500, height=500, bg="white")
frame3 = Frame(my_notebook, width=500, height=500, bg="white")
frame4 = Frame(my_notebook, width=500, height=500, bg="white")
frame5 = Frame(my_notebook, width=500, height=500, bg="white")
frame6 = Frame(my_notebook, width=500, height=500, bg = "white")


# STAVLJANJE FRAME-ova NA GUI
frame.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)
frame6.pack(fill="both", expand=1)

# ATRIBUTI FRAME-ova
my_notebook.add(frame, text="Igraci")
my_notebook.add(frame2, text="Treneri")
my_notebook.add(frame3, text="Sesije")
my_notebook.add(frame4, text="Sudci")
my_notebook.add(frame5, text="Timovi")
my_notebook.add(frame6, text="Extra")

test_label = Label(frame5, text="No records to show", bg="white")

root.mainloop()
