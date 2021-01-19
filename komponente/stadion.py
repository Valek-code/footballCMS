
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


#dohvaca sve sudce i ispisuje ih na zaseban prozor
def pokaziStadione():
    prikaziStadione = Tk()
    prikaziStadione.title("Lista stadiona")
    prikaziStadione.geometry("400x500")

    cursor.execute("SELECT * FROM stadion")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):
        cursor2.execute(f'SELECT ime FROM grad WHERE id = {rezultat[3]}')
        gradRez = cursor2.fetchone()
        test_label = Label(prikaziStadione, text=f"[ID:{rezultat[0]}]. {rezultat[1]} => {gradRez[0]} [ KAPACITET GLEDATELJA: {rezultat[2]}]", bg="white")
        test_label.pack()


# dodaje sudca koji puni korisnik sucelja custom podacima
def dodajStadione():

    def stadionToDb(naziv, kapacitet, id_grad):
        try:
            if not kapacitet or kapacitet == '':
                alertWindow('Kapacitet mora biti naznačen')
                return
            cursor.execute(f"""INSERT INTO stadion(naziv, kapacitet_gledatelja, id_grad) 
                                    VALUES("{naziv}",{kapacitet},{id_grad})""")
            db.commit()
            clear()
            alertWindow(f"Stadion {ime} uspjesno dodan u bazu podataka!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def clear():
        entry_ime.delete(0, END)

    def getGradIDFromName():
        izbor = lista_gradova.get(lista_gradova.curselection())
        cursor.execute(f"SELECT * FROM grad WHERE ime = '{izbor}'")
        id = cursor.fetchone()
        return id[0]

    dodajStadion = Tk()
    dodajStadion.title("Dodaj stadion")
    dodajStadion.geometry("200x300")

    label_ime = Label(dodajStadion, text="Naziv")
    label_ime.grid(row=0, column=0)

    entry_ime = Entry(dodajStadion)
    entry_ime.grid(row= 0, column=1)

    label_kapacitet = Label(dodajStadion, text="Kapacitet gledatelja:")
    label_kapacitet.grid(row=1, column=1)

    entry_kapacitet = Entry(dodajStadion)
    entry_kapacitet.grid(row=1, column=1)

    lista_gradova = Label(dodajStadion, text="Grad")
    lista_gradova.grid(row=2, column=0)

    lista_gradova = Listbox(dodajStadion, exportselection=0)
    lista_gradova.grid(row=2, column=1)


    dodajStadionGumb = Button(dodajStadion, text="Dodaj", command=lambda:stadionToDb(entry_ime.get(), entry_kapacitet.get(), getGradIDFromName ))
    dodajStadionGumb.grid(row=5, column=1, columnspan=2)

    popuniGradIzbor(lista_gradova)


def deleteStadionEntry():

    def deleteStadion():
        try:
            izbor = lista_gradova.get(lista_gradova.curselection())
            izbor_p = getIDnumFromString(izbor)
            cursor.execute(f"DELETE FROM stadion WHERE id = '{izbor_p}'")
            db.commit()
            alertWindow(f"Grad [ID:{izbor_p}] uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    deleteStadionWin = Tk()
    deleteStadionWin.title("Brisanje stadiona")
    deleteStadionWin.geometry("250x250")

    cursor.execute("SELECT * FROM stadion")
    rezultati = cursor.fetchall()


    lista_stadiona = Listbox(deleteStadionWin, exportselection=0)
    lista_stadiona.pack()

    label_upozorenje = Label(deleteStadionWin, text="Ne mozete brisati slucajeve \n koji su vec u opticaju")
    label_upozorenje.pack()

    for x in rezultati:
        lista_stadiona.insert(END, f"[ID:{x[0]}] {x[1]}")

    brisiGumb = Button(deleteStadionWin, text="Izbrisi", pady=5, command=deleteStadion)
    brisiGumb.pack()
