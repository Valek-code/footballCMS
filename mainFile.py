from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import csv
from komponente import timovi, igraci, treneri, sesije, sudac, selekcije, drzave, gradovi, statistika

# PROZORI
root = Tk()
root.title("Baze podataka - Projekt")
root.geometry("500x500")


# NOTEBOOK
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)


# FRAMEOVI ( TABOVI )
frame = Frame(my_notebook, width=1920, height=1080, bg="white")
frame2 = Frame(my_notebook, width=1920, height=1080, bg="white")
frame3 = Frame(my_notebook, width=1920, height=1080, bg="white")
frame4 = Frame(my_notebook, width=1920, height=1080, bg="white")
frame5 = Frame(my_notebook, width=1920, height=1080, bg="white")
frame6 = Frame(my_notebook, width=1920, height=1080, bg = "white")
frame7 = Frame(my_notebook, width=1920, height=1080, bg = "white")
frame8 = Frame(my_notebook, width=1920, height=1080, bg = "white")
frame9 = Frame(my_notebook, width=1920, height=1080, bg = "white")


# STAVLJANJE FRAME-ova NA GUI
frame.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)
frame6.pack(fill="both", expand=1)
frame7.pack(fill="both", expand=1)
frame8.pack(fill="both", expand=1)
frame9.pack(fill="both", expand=1)

# ATRIBUTI FRAME-ova
my_notebook.add(frame, text="Igraci")
my_notebook.add(frame2, text="Treneri")
my_notebook.add(frame3, text="Sesije")
my_notebook.add(frame4, text="Sudci")
my_notebook.add(frame5, text="Timovi")
my_notebook.add(frame6, text="Drzave")
my_notebook.add(frame7, text="Gradovi")
my_notebook.add(frame8, text="Statistika")
my_notebook.add(frame9, text="Extra")

test_label = Label(frame5, text="No records to show", bg="white")


# gumbi frame 5
dodaj_klub_gumb = Button(frame5, text="Dodaj tim", pady=15, padx=250, command=timovi.dodajTim)
prikazi_klubove_gumb = Button(frame5, text="Prikazi timove", pady=15, padx=250, command=timovi.showTeams)
izbrisi_tim_gumb = Button(frame5, text="Brisanje timova", pady=15, padx=250, command=timovi.deleteTeamEntry)

dodaj_klub_gumb.pack()
prikazi_klubove_gumb.pack()
izbrisi_tim_gumb.pack()


# gumbi frame 4
dodaj_sudca_gumb = Button(frame4, text="Dodaj sudca", pady=15, padx=250, command=sudac.dodajSudca)
prikazi_sudce_gumb = Button(frame4, text="Prikazi sve sudce", pady=15, padx=250, command=sudac.pokaziSudce)
izbrisi_sudce_gumb = Button(frame4, text="Brisanje sudaca", pady=15, padx=250, command=sudac.deleteSudacEntry)

dodaj_sudca_gumb.pack()
prikazi_sudce_gumb.pack()
izbrisi_sudce_gumb.pack()

# gumbi frame 6
dodaj_drzavu_gumb = Button(frame6, text="Dodaj drzavu", pady=15, padx=250, command=drzave.dodajDrzave)
prikazi_drzave_gumb = Button(frame6, text="Prikazi sve drzave", pady=15, padx=250, command=drzave.pokaziDrzave)
izbrisi_drzave_gumb = Button(frame6, text="Brisanje drzava", pady=15, padx=250, command=drzave.deleteDrzavaEntry)

dodaj_drzavu_gumb.pack()
prikazi_drzave_gumb.pack()
izbrisi_drzave_gumb.pack()

# gumbi frame 7
dodaj_grad_gumb = Button(frame7, text="Dodaj grad", pady=15, padx=250, command=gradovi.dodajGradove)
prikazi_gradove_gumb = Button(frame7, text="Prikazi sve gradove", pady=15, padx=250, command=gradovi.pokaziGradove)
izbrisi_gradove_gumb = Button(frame7, text="Brisanje gradova", pady=15, padx=250, command=gradovi.deleteGradEntry)

dodaj_grad_gumb.pack()
prikazi_gradove_gumb.pack()
izbrisi_gradove_gumb.pack()

# gumbi frame 8
trazistatistiku_label = Label(frame8, text="ID SESIJE: ")
trazistatistiku_label.grid(row=0, column=0)

trazistatistiku_entry = Entry(frame8)
trazistatistiku_entry.grid(row=0, column=1)

traziStatistikuGumb = Button(frame8, text="Trazi", pady=15, padx=250, command=lambda:statistika.traziStatisiku(trazistatistiku_entry.get()))
traziStatistikuGumb.grid(row=1, column=0,columnspan=12)

# gumbi frame 2
dodaj_trenere_gumb = Button(frame2, text="Dodaj trenera", pady=15, padx=250, command=treneri.dodajTrenera)
prikazi_trenere_gumb = Button(frame2, text="Prikazi sve trenere", pady=15, padx=250, command=treneri.pokaziTrenere)
izbrisi_trenere_gumb = Button(frame2, text="Brisanje trenera", pady=15, padx=250, command=treneri.deleteTrenerEntry)

dodaj_trenere_gumb.pack()
prikazi_trenere_gumb.pack()
izbrisi_trenere_gumb.pack()


# gumbi frame 1
dodaj_igraca_gumb = Button(frame, text="Dodaj igraca", pady=15, padx=250, command=igraci.dodajIgrace)
prikazi_igrace_gumb = Button(frame, text="Prikazi sve igrace", pady=15, padx=250, command=igraci.pokaziIgrace)
izbrisi_igraca_gumb = Button(frame, text="Brisanje igraca", pady=15, padx=250, command=igraci.deleteIgracEntry)

dodaj_igraca_gumb.pack()
prikazi_igrace_gumb.pack()
izbrisi_igraca_gumb.pack()

# gumbi frame 3
dodaj_sesija_gumb = Button(frame3, text="Dodaj sesiju", pady=15, padx=250, command=sesije.dodajSesiju)
prikazi_sesije_gumb = Button(frame3, text="Prikazi sve sesije", pady=15, padx=250, command=sesije.pokaziSesije)
izbrisi_sesija_gumb = Button(frame3, text="Brisanje sesija", pady=15, padx=250, command=sesije.deleteSesijaEntry)

dodaj_sesija_gumb.pack()
prikazi_sesije_gumb.pack()
izbrisi_sesija_gumb.pack()

root.mainloop()