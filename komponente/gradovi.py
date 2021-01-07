
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


#dohvaca sve sudce i ispisuje ih na zaseban prozor
def pokaziGradove():
    prikaziGradove = Tk()
    prikaziGradove.title("Lista gradova")
    prikaziGradove.geometry("250x500")

    cursor.execute("SELECT * FROM grad")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(prikaziGradove, text=f"{index+1}. {rezultat[1]}", bg="white")
        test_label.pack()


# dodaje sudca koji puni korisnik sucelja custom podacima
def dodajGradove():

    def gradToDb(ime):
        cursor.execute(f"""INSERT INTO grad(ime) 
                                VALUES("{ime}")""")
        db.commit()
        clear()
        alertWindow(f"Grad {ime} uspjesno dodan u bazu podataka!")

    def clear():
        entry_ime.delete(0, END)

    dodajGrad = Tk()
    dodajGrad.title("Dodaj grad")
    dodajGrad.geometry("250x500")

    label_ime = Label(dodajGrad, text="Ime")
    label_ime.grid(row=0, column=0)

    entry_ime = Entry(dodajGrad)
    entry_ime.grid(row= 0, column=1)

    dodajGradGumb = Button(dodajGrad, text="Dodaj", command=lambda:gradToDb(entry_ime.get()))
    dodajGradGumb.grid(row=5, column=1, columnspan=2)


# brise sudca iz baze
def deleteGradEntry():

    def deleteGrad():
        izbor = lista_gradova.get(lista_gradova.curselection())
        cursor.execute(f"DELETE FROM grad WHERE ime = '{izbor}'")
        db.commit()
        alertWindow(f"Grad {izbor} uspjesno izbrisan!")

    deleteGradWin = Tk()
    deleteGradWin.title("Brisanje gradova")
    deleteGradWin.geometry("250x250")

    cursor.execute("SELECT * FROM grad")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o sudcima
    lista_gradova = Listbox(deleteGradWin, exportselection=0)
    lista_gradova.pack()

    # puni se selekcija za brisanje sudaca
    for x in rezultati:
        lista_gradova.insert(END, f"{x[1]}")

    brisiGumb = Button(deleteGradWin, text="Izbrisi", pady=5, command=deleteGrad)
    brisiGumb.pack()
