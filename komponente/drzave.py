
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


def updateDrzave():

    def updateDrzavaFunc(_id, _ime):
        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"UPDATE drzava SET ime = '{_ime}' WHERE id = {_id}")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    updateDrzaveWin = Tk()
    updateDrzaveWin.title("Update drzava")
    updateDrzaveWin.geometry("250x300")

    label_id = Label(updateDrzaveWin, text="Ime države: ")
    label_id.grid(row=0, column=0)

    entry_idDrzave = Entry(updateDrzaveWin)
    entry_idDrzave.grid(row=0, column=1)

    label_ime = Label(updateDrzaveWin, text="Novo ime države: ")
    label_ime.grid(row=1, column=0)

    entry_ime = Entry(updateDrzaveWin)
    entry_ime.grid(row=1, column=1)

    updejtajDrzavuGumb = Button(updateDrzaveWin, text="Update", command=lambda: updateDrzavaFunc(entry_idDrzave.get(), entry_ime.get()))
    updejtajDrzavuGumb.grid(row=2, column=1, columnspan=2)


#dohvaca sve sudce i ispisuje ih na zaseban prozor
def pokaziDrzave():
    prikaziDrzave = Tk()
    prikaziDrzave.title("Lista drzava")
    prikaziDrzave.geometry("250x500")

    cursor.execute("SELECT * FROM drzava")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(prikaziDrzave, text=f"ID:{rezultat[0]}. {rezultat[1]}", bg="white")
        test_label.pack()


# dodaje sudca koji puni korisnik sucelja custom podacima
def dodajDrzave():

    def drzavaToDb(ime):
        try:
            cursor.execute(f"""INSERT INTO drzava(ime) 
                                    VALUES("{ime}")""")
            db.commit()
            clear()
            alertWindow(f"Drzava {ime} uspjesno dodana u bazu podataka!")

        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

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
        try:
            izbor = lista_drzava.get(lista_drzava.curselection())
            cursor.execute(f"DELETE FROM drzava WHERE ime = '{izbor}'")
            db.commit()
            alertWindow(f"Drzava {izbor} uspjesno izbrisana!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

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
