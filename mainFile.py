from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import csv
from komponente import timovi, igraci, treneri, sesije, sudac, selekcije

# PROZORI
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


# gumbi frame 5
dodaj_klub_gumb = Button(frame5, text="Dodaj tim", pady=5, command=timovi.dodajTim)
prikazi_klubove_gumb = Button(frame5, text="Prikazi timove", pady=5, command=timovi.showTeams)
izbrisi_tim_gumb = Button(frame5, text="Brisanje timova", pady=5, command=timovi.deleteTeamEntry)

dodaj_klub_gumb.pack()
prikazi_klubove_gumb.pack()
izbrisi_tim_gumb.pack()


# gumbi frame 4
dodaj_sudca_gumb = Button(frame4, text="Dodaj sudca", pady=5, command=sudac.dodajSudca)
prikazi_sudce_gumb = Button(frame4, text="Prikazi sve sudce", pady=5, command=sudac.pokaziSudce)
izbrisi_sudce_gumb = Button(frame4, text="Brisanje sudaca", pady=5, command=sudac.deleteSudacEntry)

dodaj_sudca_gumb.pack()
prikazi_sudce_gumb.pack()
izbrisi_sudce_gumb.pack()


# gumbi frame 2
dodaj_trenere_gumb = Button(frame2, text="Dodaj trenera", pady=5, command=treneri.dodajTrenera)
prikazi_trenere_gumb = Button(frame2, text="Prikazi sve trenere", pady=5, command=treneri.pokaziTrenere)
izbrisi_trenere_gumb = Button(frame2, text="Brisanje trenera", pady=5, command=treneri.deleteTrenerEntry)

dodaj_trenere_gumb.pack()
prikazi_trenere_gumb.pack()
izbrisi_trenere_gumb.pack()


# gumbi frame 1
dodaj_igraca_gumb = Button(frame, text="Dodaj igraca", pady=5, command=igraci.dodajIgrace)
prikazi_igrace_gumb = Button(frame, text="Prikazi sve igrace", pady=5, command=igraci.pokaziIgrace)
izbrisi_igraca_gumb = Button(frame, text="Brisanje igraca", pady=5, command=igraci.deleteIgracEntry)

dodaj_igraca_gumb.pack()
prikazi_igrace_gumb.pack()
izbrisi_igraca_gumb.pack()

# gumbi frame 3
dodaj_sesija_gumb = Button(frame3, text="Dodaj sesiju", pady=5, command=sesije.dodajSesiju)
prikazi_sesije_gumb = Button(frame3, text="Prikazi sve sesije", pady=5, command=sesije.pokaziSesije)
izbrisi_sesija_gumb = Button(frame3, text="Brisanje sesija", pady=5, command=sesije.deleteSesijaEntry)

dodaj_sesija_gumb.pack()
prikazi_sesije_gumb.pack()
izbrisi_sesija_gumb.pack()

root.mainloop()