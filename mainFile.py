from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import csv
from komponente import timovi, igraci, treneri, sesije, sudac, selekcije, drzave, gradovi, statistika, stadion, gol, udarci, out

# PROZORI
root = Tk()
root.title("Baze podataka - Projekt")
root.geometry("520x520")

canvas = Canvas(root, width = 200, height = 200)
canvas.pack()
img = PhotoImage(file="logo.png")
canvas.create_image(0,0, anchor=NW, image=img)

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
frame10 = Frame(my_notebook, width=1920, height=1080, bg = "white")
frame11 = Frame(my_notebook, width=1920, height=1080, bg = "white")
frame12 = Frame(my_notebook, width=1920, height=1080, bg = "white")
frame13 = Frame(my_notebook, width=1920, height=1080, bg = "white")


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
frame10.pack(fill="both", expand=1)
frame11.pack(fill="both", expand=1)
frame12.pack(fill="both", expand=1)
frame13.pack(fill="both", expand=1)

# ATRIBUTI FRAME-ova
my_notebook.add(frame, text="Drzave")
my_notebook.add(frame2, text="Gradovi")
my_notebook.add(frame3, text="Stadion")
my_notebook.add(frame4, text="Treneri")
my_notebook.add(frame5, text="Timovi")
my_notebook.add(frame6, text="Igraci")
my_notebook.add(frame7, text="Sudci")
my_notebook.add(frame8, text="Sesije")
my_notebook.add(frame9, text="Gol")
my_notebook.add(frame10, text="Out")
my_notebook.add(frame11, text="Udarac")
my_notebook.add(frame12, text="Statistika")
my_notebook.add(frame13, text="Extra")



test_label = Label(frame5, text="No records to show", bg="white")


# gumbi frame 5
dodaj_klub_gumb = Button(frame5, text="Dodaj tim", pady=15, padx=250, command=timovi.dodajTim)
prikazi_klubove_gumb = Button(frame5, text="Prikazi timove", pady=15, padx=250, command=timovi.showTeams)
izbrisi_tim_gumb = Button(frame5, text="Brisanje timova", pady=15, padx=250, command=timovi.deleteTeamEntry)
update_tim_gumb = Button(frame5, text="Update timova", pady=15, padx=250, command=timovi.UpdateTim)

dodaj_klub_gumb.pack()
prikazi_klubove_gumb.pack()
izbrisi_tim_gumb.pack()
update_tim_gumb.pack()

# gumbi frame 4
dodaj_sudca_gumb = Button(frame7, text="Dodaj sudca", pady=15, padx=250, command=sudac.dodajSudca)
prikazi_sudce_gumb = Button(frame7, text="Prikazi sve sudce", pady=15, padx=250, command=sudac.pokaziSudce)
izbrisi_sudce_gumb = Button(frame7, text="Brisanje sudaca", pady=15, padx=250, command=sudac.deleteSudacEntry)
update_sudce_gumb = Button(frame7, text="Update sudaca", pady=15, padx=250, command=sudac.updatesudac)

dodaj_sudca_gumb.pack()
prikazi_sudce_gumb.pack()
izbrisi_sudce_gumb.pack()
update_sudce_gumb.pack()

# gumbi frame 6
dodaj_drzavu_gumb = Button(frame, text="Dodaj drzavu", pady=15, padx=250, command=drzave.dodajDrzave)
prikazi_drzave_gumb = Button(frame, text="Prikazi sve drzave", pady=15, padx=250, command=drzave.pokaziDrzave)
izbrisi_drzave_gumb = Button(frame, text="Brisanje drzava", pady=15, padx=250, command=drzave.deleteDrzavaEntry)
update_drzave_gumb = Button(frame, text="Update drzava", pady=15, padx=250, command=drzave.updateDrzave)

dodaj_drzavu_gumb.pack()
prikazi_drzave_gumb.pack()
izbrisi_drzave_gumb.pack()
update_drzave_gumb.pack()

# gumbi frame 7
dodaj_grad_gumb = Button(frame2, text="Dodaj grad", pady=15, padx=250, command=gradovi.dodajGradove)
prikazi_gradove_gumb = Button(frame2, text="Prikazi sve gradove", pady=15, padx=250, command=gradovi.pokaziGradove)
izbrisi_gradove_gumb = Button(frame2, text="Brisanje gradova", pady=15, padx=250, command=gradovi.deleteGradEntry)
update_gradove_gumb = Button(frame2, text="Update gradova", pady=15, padx=250, command=gradovi.updateGrad)


dodaj_grad_gumb.pack()
prikazi_gradove_gumb.pack()
izbrisi_gradove_gumb.pack()
update_gradove_gumb.pack()

# gumbi frame 8
trazistatistiku_label = Label(frame12, text="ID SESIJE: ")
trazistatistiku_label.grid(row=0, column=0)

trazistatistiku_entry = Entry(frame12)
trazistatistiku_entry.grid(row=0, column=1)

traziStatistikuGumb = Button(frame12, text="Trazi", pady=15, padx=250, command=lambda:statistika.traziStatisiku(trazistatistiku_entry.get()))
ispisiStatistikuGumbXlsx = Button(frame12, text="Ispis - XLSX", pady=15, padx=250, command=lambda:statistika.spremiStatistiku(trazistatistiku_entry.get()))
ispisiStatistikuGumbTxt = Button(frame12, text="Ispis - TXT", pady=15, padx=250, command=lambda:statistika.SpremiStatistikuTxt(trazistatistiku_entry.get()))

traziStatistikuGumb.grid(row=1, column=0,columnspan=12)
ispisiStatistikuGumbXlsx.grid(row=2, column=0,columnspan=12)
ispisiStatistikuGumbTxt.grid(row=3, column=0,columnspan=12)

# gumbi frame 2
dodaj_trenere_gumb = Button(frame4, text="Dodaj trenera", pady=15, padx=250, command=treneri.dodajTrenera)
prikazi_trenere_gumb = Button(frame4, text="Prikazi sve trenere", pady=15, padx=250, command=treneri.pokaziTrenere)
izbrisi_trenere_gumb = Button(frame4, text="Brisanje trenera", pady=15, padx=250, command=treneri.deleteTrenerEntry)
update_trenere_gumb = Button(frame4, text="Update trenera", pady=15, padx=250, command=treneri.updatetrener)

dodaj_trenere_gumb.pack()
prikazi_trenere_gumb.pack()
izbrisi_trenere_gumb.pack()
update_trenere_gumb.pack()

# gumbi frame 1
dodaj_igraca_gumb = Button(frame6, text="Dodaj igraca", pady=15, padx=250, command=igraci.dodajIgrace)
prikazi_igrace_gumb = Button(frame6, text="Prikazi sve igrace", pady=15, padx=250, command=igraci.pokaziIgrace)
izbrisi_igraca_gumb = Button(frame6, text="Brisanje igraca", pady=15, padx=250, command=igraci.deleteIgracEntry)
update_igraca_gumb = Button(frame6, text="Update igraca", pady=15, padx=250, command=igraci.updateIgrac)

dodaj_igraca_gumb.pack()
prikazi_igrace_gumb.pack()
izbrisi_igraca_gumb.pack()
update_igraca_gumb.pack()

# gumbi frame 3
dodaj_sesija_gumb = Button(frame8, text="Dodaj sesiju", pady=15, padx=250, command=sesije.dodajSesiju)
prikazi_sesije_gumb = Button(frame8, text="Prikazi sve sesije", pady=15, padx=250, command=sesije.pokaziSesije)
izbrisi_sesija_gumb = Button(frame8, text="Brisanje sesija", pady=15, padx=250, command=sesije.deleteSesijaEntry)
update_sesija_gumb = Button(frame8, text="Update sesija", pady=15, padx=250, command=sesije.updateSesija)

dodaj_sesija_gumb.pack()
prikazi_sesije_gumb.pack()
izbrisi_sesija_gumb.pack()
update_sesija_gumb.pack()

# gumbi frame stadion
dodaj_stadion_gumb = Button(frame3, text="Dodaj stadion", pady=15, padx=250, command=stadion.dodajStadione)
prikazi_stadione_gumb = Button(frame3, text="Prikazi sve stadione", pady=15, padx=250, command=stadion.pokaziStadione)
izbrisi_stadione_gumb = Button(frame3, text="Brisanje stadiona", pady=15, padx=250, command=stadion.deleteStadionEntry)
update_stadione_gumb = Button(frame3, text="Update stadiona", pady=15, padx=250, command=stadion.updateStadion)

dodaj_stadion_gumb.pack()
prikazi_stadione_gumb.pack()
izbrisi_stadione_gumb.pack()
update_stadione_gumb.pack()
# gumbi frame gol

dodajGolSesiji_label = Label(frame9, text="ID SESIJE: ")
dodajGolSesiji_label.pack()

dobiIdSesije_entry = Entry(frame9)
dobiIdSesije_entry.pack()

dodaj_gol_gumb = Button(frame9, text="Dodaj gol", pady=15, padx=250, command=lambda:gol.dodajGolove(dobiIdSesije_entry.get()))
prikazi_golove_gumb = Button(frame9, text="Prikazi sve golove", pady=15, padx=250, command=lambda:gol.prikaziSveGolovePoSesiji(dobiIdSesije_entry.get()))
izbrisi_golove_gumb = Button(frame9, text="Brisanje golova", pady=15, padx=250, command=lambda:gol.deleteGolEntry(dobiIdSesije_entry.get()))
update_gol_gumb = Button(frame9, text="Update golova(ID NOT REQ*)", pady=15, padx=250, command=gol.updateGolove)

dodaj_gol_gumb.pack()
prikazi_golove_gumb.pack()
izbrisi_golove_gumb.pack()
update_gol_gumb.pack()


# gumbi frame udarci

dodaj_udarce_sesiji = Label(frame11, text="ID SESIJE: ")
dodaj_udarce_sesiji.pack()

dobiIdSesije_udarci_entry = Entry(frame11)
dobiIdSesije_udarci_entry.pack()

dodaj_udarce_gumb = Button(frame11, text="Dodaj zapis o udarcima", pady=15, padx=250, command=lambda:udarci.dodajUdarce(dobiIdSesije_udarci_entry.get()))
prikazi_udarce_gumb = Button(frame11, text="Prikaz svih udaraca", pady=15, padx=250, command=lambda:udarci.prikaziSveUdarcePoSesiji(dobiIdSesije_udarci_entry.get()))
izbrisi_udarce_gumb = Button(frame11, text="Brisanje zapisa o udarcima", pady=15, padx=250, command=lambda:udarci.deleteUdaracEntry(dobiIdSesije_udarci_entry.get()))
update_udarce_gumb = Button(frame11, text="Update zapisa o udarcima", pady=15, padx=250, command=udarci.updateUdarce)


dodaj_udarce_gumb.pack()
prikazi_udarce_gumb.pack()
izbrisi_udarce_gumb.pack()
update_udarce_gumb.pack()

# gumbi frame outevi

dodaj_outeve_sesiji = Label(frame10, text="ID SESIJE: ")
dodaj_outeve_sesiji.pack()

dobiIdSesije_outevi_entry = Entry(frame10)
dobiIdSesije_outevi_entry.pack()

dodaj_outeve_gumb = Button(frame10, text="Dodaj zapis o outevima", pady=15, padx=250, command=lambda:out.dodajOut(dobiIdSesije_outevi_entry.get()))
prikazi_outeve_gumb = Button(frame10, text="Prikaz svih outeva", pady=15, padx=250, command=lambda:out.prikaziSveOutovePoSesiji(dobiIdSesije_outevi_entry.get()))
izbrisi_outeve_gumb = Button(frame10, text="Brisanje zapisa o outevima", pady=15, padx=250, command=lambda:out.deleteOuteviEntry(dobiIdSesije_outevi_entry.get()))
update_outeve_gumb = Button(frame10, text="Update zapisa o outevima", pady=15, padx=250, command=out.updateOutove)

dodaj_outeve_gumb.pack()
prikazi_outeve_gumb.pack()
izbrisi_outeve_gumb.pack()
update_outeve_gumb.pack()

root.mainloop()