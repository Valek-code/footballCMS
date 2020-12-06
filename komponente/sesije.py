
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


#dohvaca sve sesije i ispisuje ih na zaseban prozor
def pokaziSesije():
    sesije = Tk()
    sesije.title("Lista svih sesija")
    sesije.geometry("250x500")

    cursor.execute("SELECT * FROM sesija")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):
        cursor2.execute(f"SELECT ime FROM tim WHERE id = {rezultat[1]}")
        ime1 = cursor2.fetchone()
        cursor2.execute(f"SELECT ime FROM tim where id = {rezultat[2]}")
        ime2 = cursor2.fetchone()
        test_label = Label(sesije, text=f"ID: {rezultat[0]} | {ime1[0]} VS {ime2[0]}", bg="white")
        test_label.pack()


# dodaje sesiju koju puni korisnik sucelja custom podacima
def dodajSesiju():

    def sesijaToDb(tim1_id, tim2_id):
        cursor.execute(f"""INSERT INTO sesija(tim1_id,tim2_id) 
                                VALUES("{tim1_id}","{tim2_id}")""")
        db.commit()
        clear()

    def clear():
        lista_timova1.delete(0, END)
        lista_timova2.delete(0, END)

    def dobiIDtima():
        izbor = lista_timova1.get(lista_timova1.curselection())
        cursor.execute(f"SELECT * FROM tim WHERE ime = '{izbor}'")
        id = cursor.fetchone()
        return id[0]

    def dobiIDtima2():
        izbor = lista_timova2.get(lista_timova2.curselection())
        cursor.execute(f"SELECT * FROM tim WHERE ime = '{izbor}'")
        id = cursor.fetchone()
        return id[0]

    dodaj_sesiju = Tk()
    dodaj_sesiju.title("Dodaj sesiju")
    dodaj_sesiju.geometry("250x500")

    label_tim1 = Label(dodaj_sesiju, text="Tim 1")
    label_tim1.grid(row=0, column=0)

    label_tim2 = Label(dodaj_sesiju, text="Tim 2")
    label_tim2.grid(row=1, column=0)

    lista_timova1 = Listbox(dodaj_sesiju, exportselection=0)
    lista_timova1.grid(row=0, column=1)

    lista_timova2 = Listbox(dodaj_sesiju, exportselection=0)
    lista_timova2.grid(row=1, column=1)

    popuniTimoveIzbor(lista_timova1)
    popuniTimoveIzbor(lista_timova2)

    dodajIgraca_gumb = Button(dodaj_sesiju, text="Dodaj", command=lambda:sesijaToDb(dobiIDtima(), dobiIDtima2()))
    dodajIgraca_gumb.grid(row=6, column=1, columnspan=2)


# brise sesije iz baze
def deleteSesijaEntry():

    def deleteSesija():
        izbor = lista_sesija.get(lista_sesija.curselection())
        cursor.execute(f"DELETE FROM sesija WHERE id = '{izbor}'")
        db.commit()
        alertWindow(f"Sesija {izbor} uspjesno izbrisan!")

    deleteSesijaWin = Tk()
    deleteSesijaWin.title("Brisanje Sesija")
    deleteSesijaWin.geometry("250x500")

    cursor.execute("SELECT * FROM sesija")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o sesijama
    lista_sesija = Listbox(deleteSesijaWin, exportselection=0)
    lista_sesija.pack()

    # puni se selekcija za brisanje sesija
    for x in rezultati:
        lista_sesija.insert(END, f"{x[1]}")

    brisiGumb = Button(deleteSesijaWin, text="Izbrisi", pady=5, command=deleteSesija)
    brisiGumb.pack()
