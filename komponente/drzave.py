
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


#dohvaca sve sudce i ispisuje ih na zaseban prozor
def pokaziDrzave():
    prikaziDrzave = Tk()
    prikaziDrzave.title("Lista drzava")
    prikaziDrzave.geometry("250x500")

    cursor.execute("SELECT * FROM drzava")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(prikaziDrzave, text=f"{index+1}. {rezultat[1]}", bg="white")
        test_label.pack()


# dodaje sudca koji puni korisnik sucelja custom podacima
def dodajDrzave():

    def drzavaToDb(ime):
        cursor.execute(f"""INSERT INTO drzava(ime) 
                                VALUES("{ime}")""")
        db.commit()
        clear()
        alertWindow(f"Drzava {ime} uspjesno dodana u bazu podataka!")

    def clear():
        entry_ime.delete(0, END)

    dodajDrzavu = Tk()
    dodajDrzavu.title("Dodaj drzavu")
    dodajDrzavu.geometry("250x500")

    label_ime = Label(dodajDrzavu, text="Ime")
    label_ime.grid(row=0, column=0)

    entry_ime = Entry(dodajDrzavu)
    entry_ime.grid(row= 0, column=1)

    dodajDrzavuGumb = Button(dodajDrzavu, text="Dodaj", command=lambda:drzavaToDb(entry_ime.get()))
    dodajDrzavuGumb.grid(row=5, column=1, columnspan=2)


# brise sudca iz baze
def deleteDrzavaEntry():

    def deleteDrzava():
        izbor = lista_drzava.get(lista_drzava.curselection())
        cursor.execute(f"DELETE FROM drzava WHERE ime = '{izbor}'")
        db.commit()
        alertWindow(f"Drzava {izbor} uspjesno izbrisana!")

    deleteDrzavaWin = Tk()
    deleteDrzavaWin.title("Brisanje drzave")
    deleteDrzavaWin.geometry("250x250")

    cursor.execute("SELECT * FROM drzava")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o sudcima
    lista_drzava = Listbox(deleteDrzavaWin, exportselection=0)
    lista_drzava.pack()

    # puni se selekcija za brisanje sudaca
    for x in rezultati:
        lista_drzava.insert(END, f"{x[1]}")

    brisiGumb = Button(deleteDrzavaWin, text="Izbrisi", pady=5, command=deleteDrzava)
    brisiGumb.pack()
