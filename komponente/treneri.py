
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


#dohvaca sve trenere i ispisuje ih na zaseban prozor
def pokaziTrenere():
    treneri = Tk()
    treneri.title("Lista trenera")
    treneri.geometry("250x500")

    cursor.execute("SELECT * FROM trener")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(treneri, text=f"{rezultat[0]}. {rezultat[1]} | {rezultat[2]} | {rezultat[3]} | {rezultat[4]} | {rezultat[5]} | {rezultat[6]}", bg="white")
        test_label.pack()


# dodaje trenera koji puni korisnik sucelja custom podacima
def dodajTrenera():

    def trenerToDb(ime, prezime, datum_rodenja, drzava, grad, tim):
        cursor.execute(f"""INSERT INTO trener(ime,prezime,datum_rodenja,id_drzava, id_grad, id_tim) 
                                VALUES("{ime}","{prezime}",str_to_date('{datum_rodenja}','%d/%m/%Y'),{drzava}, {grad}, {tim})""")
        db.commit()
        clear()

    def clear():
        entry_ime.delete(0, END)
        entry_prezime.delete(0, END)
        entry_dr.delete(0,END)
        lista_gradova.selection_clear(0, END)
        lista_drzava.selection_clear(0, END)
        lista_timova.selection_clear(0, END)

    def dobiIDtima():
        izbor = lista_timova.get(lista_timova.curselection())
        cursor.execute(f"SELECT * FROM tim WHERE ime = '{izbor}'")
        id = cursor.fetchone()
        return id[0]


    dodaj_trenera = Tk()
    dodaj_trenera.title("Dodaj trenera")
    dodaj_trenera.geometry("250x800")

    label_ime = Label(dodaj_trenera, text="Ime")
    label_ime.grid(row=0, column=0)

    label_prezime = Label(dodaj_trenera, text="Prezime")
    label_prezime.grid(row=1, column=0)

    label_dr = Label(dodaj_trenera, text="Datum_rodenja\n(dd/mm/yyyy)")
    label_dr.grid(row=2, column=0)

    label_drzava = Label(dodaj_trenera, text="Drzava")
    label_drzava.grid(row=3, column=0)

    label_grad = Label(dodaj_trenera, text="Grad")
    label_grad.grid(row=4, column=0)

    label_tim = Label(dodaj_trenera, text="Tim")
    label_tim.grid(row=5, column=0)


    entry_ime = Entry(dodaj_trenera)
    entry_ime.grid(row= 0, column=1)

    entry_prezime = Entry(dodaj_trenera)
    entry_prezime.grid(row=1, column=1)

    entry_dr = Entry(dodaj_trenera)
    entry_dr.grid(row=2, column=1)

    lista_drzava = Listbox(dodaj_trenera, exportselection=0)
    lista_drzava.grid(row=3, column=1)

    lista_gradova = Listbox(dodaj_trenera, exportselection=0)
    lista_gradova.grid(row=4, column=1)

    lista_timova = Listbox(dodaj_trenera, exportselection=0)
    lista_timova.grid(row=5, column=1)

    popuniDrzaveIzbor(lista_drzava)
    popuniGradIzbor(lista_gradova)
    popuniTimoveIzbor(lista_timova)

    dodajSudca_gumb = Button(dodaj_trenera, text="Dodaj", command=lambda:trenerToDb(entry_ime.get(),entry_prezime.get(), entry_dr.get(), lista_drzava.curselection()[0]+1, lista_gradova.curselection()[0]+1, dobiIDtima()))
    dodajSudca_gumb.grid(row=6, column=1, columnspan=2)


# brise trenera iz baze
def deleteTrenerEntry():

    def deleteTrener():
        izbor = lista_trenera.get(lista_sudaca.curselection())
        cursor.execute(f"DELETE FROM trener WHERE ime = '{izbor}'")
        db.commit()
        alertWindow(f"Trener {izbor} uspjesno izbrisan!")

    deleteSudacWin = Tk()
    deleteSudacWin.title("Brisanje Trenera")
    deleteSudacWin.geometry("250x250")

    cursor.execute("SELECT * FROM trener")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o trenerima
    lista_trenera = Listbox(deleteSudacWin, exportselection=0)
    lista_trenera.pack()

    # puni se selekcija za brisanje trenera
    for x in rezultati:
        lista_trenera.insert(END, f"{x[1]}")

    brisiGumb = Button(deleteSudacWin, text="Izbrisi", pady=5, command=deleteTrener)
    brisiGumb.pack()
