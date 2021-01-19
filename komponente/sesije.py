
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

    def sesijaToDb(tim1_id, tim2_id, id_sudac, id_stadion, datumSesije):
        try:
            if not datumSesije or datumSesije == '':
                alertWindow('Morate upisati datum sesije')
                return

            cursor.execute(f"""INSERT INTO sesija(id_tim1,id_tim2,id_sudac,id_stadion,datum_sesija) 
                                    VALUES({tim1_id},{tim2_id},{id_sudac},{id_stadion},STR_TO_DATE('{datumSesije}','%d/%m/%Y %H:%i'))""")
            db.commit()
            alertWindow(f'Nova sesija uspješno kreirana..')
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

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

    def dobiIDStadiona():
        izbor = lista_stadiona.get(lista_stadiona.curselection())
        cursor.execute(f"SELECT * FROM stadion WHERE naziv = '{izbor}'")
        id = cursor.fetchone()
        return id[0]

    dodaj_sesiju = Tk()
    dodaj_sesiju.title("Dodaj sesiju")
    dodaj_sesiju.geometry("250x730")

    label_tim1 = Label(dodaj_sesiju, text="Tim 1")
    label_tim1.grid(row=0, column=0)

    label_tim2 = Label(dodaj_sesiju, text="Tim 2")
    label_tim2.grid(row=1, column=0)

    lista_timova1 = Listbox(dodaj_sesiju, exportselection=0)
    lista_timova1.grid(row=0, column=1)

    lista_timova2 = Listbox(dodaj_sesiju, exportselection=0)
    lista_timova2.grid(row=1, column=1)

######################################################################

    label_stadion = Label(dodaj_sesiju, text="Stadion: ")
    label_stadion.grid(row=2, column=0)

    label_sudac = Label(dodaj_sesiju, text="Sudac[ID]: ")
    label_sudac.grid(row=3, column=0)

    lista_stadiona = Listbox(dodaj_sesiju, exportselection=0)
    lista_stadiona.grid(row=2, column=1)

    lista_sudaca = Listbox(dodaj_sesiju, exportselection=0)
    lista_sudaca.grid(row=3, column=1)

    label_datum = Label(dodaj_sesiju, text="Datum(dd/mm/yyyy HH:MIN): ")
    label_datum.grid(row=4, column=0)

    entry_datum = Entry(dodaj_sesiju)
    entry_datum.grid(row=4, column=1)


    popuniTimoveIzbor(lista_timova1)
    popuniTimoveIzbor(lista_timova2)
    popuniStadioneIzbor(lista_stadiona)
    popuniSudceIzbor(lista_sudaca)

    dodajIgraca_gumb = Button(dodaj_sesiju, text="Dodaj", command=lambda:sesijaToDb(dobiIDtima(), dobiIDtima2(), lista_sudaca.get(lista_sudaca.curselection()), dobiIDStadiona(),entry_datum.get()))
    dodajIgraca_gumb.grid(row=7, column=1, columnspan=2)


# brise sesije iz baze
def deleteSesijaEntry():

    def deleteSesija():
        try:
            izbor = lista_sesija.get(lista_sesija.curselection())
            cursor.execute(f"DELETE FROM sesija WHERE id = '{izbor}'")
            db.commit()
            alertWindow(f"Sesija {izbor} uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

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
        lista_sesija.insert(END, f"{x[0]}")

    brisiGumb = Button(deleteSesijaWin, text="Izbrisi", pady=5, command=deleteSesija)
    brisiGumb.pack()
