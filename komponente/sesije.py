
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
            izbor_p = getIDnumFromString(izbor)
            cursor.execute(f"DELETE FROM sesija WHERE id = '{izbor_p}'")
            db.commit()
            alertWindow(f"Sesija {izbor_p} uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    deleteSesijaWin = Tk()
    deleteSesijaWin.title("Brisanje Sesija")
    deleteSesijaWin.geometry("250x500")

    cursor.execute(
"""
SELECT s.id,t.ime,t2.ime FROM SESIJA s
JOIN tim t ON t.id = s.id_tim1
JOIN tim t2 ON t2.id = s.id_tim2;
""")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o sesijama
    lista_sesija = Listbox(deleteSesijaWin, exportselection=0, width=50)
    lista_sesija.pack()

    # puni se selekcija za brisanje sesija
    for x in rezultati:
        lista_sesija.insert(END, f"[ID:[{x[0]}] {x[1]} - {x[2]}")

    brisiGumb = Button(deleteSesijaWin, text="Izbrisi", pady=5, command=deleteSesija)
    brisiGumb.pack()


def updateSesija(): #id, id_tim1,2 id sudac id stadion datumsesija

    def updatetim1(_id, _tim1):
        if not _id or not _tim1 or _id =='' or _tim1 == '' :
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"UPDATE sesija SET id_tim1= '{_tim1}' where id = {_id}")
            db.commit()
            alertWindow(f"Podaci uspjesno izmjenjeni")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def updatetim2(_id, _tim2):
        if not _id or not _tim2 or _id =='' or _tim2 == '' :
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"""UPDATE sesija SET id_tim2= '{_tim2}' where id = {_id}""")
            db.commit()
            alertWindow(f"Podaci uspjesno izmjenjeni")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def updateSudac(_id, _idsudac):
        if not _id or not _idsudac or _id =='' or _idsudac == '' :
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"""UPDATE sesija SET id_sudac= '{_idsudac}' where id = {_id}""")
            db.commit()
            alertWindow(f"Podaci uspjesno izmjenjeni")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def updateStadion(_id, _stadion):
        if not _id or not _stadion or _id =='' or _stadion == '' :
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"""UPDATE sesija SET id_stadion= '{_stadion}' where id = {_id}""")
            db.commit()
            alertWindow(f"Podaci uspjesno izmjenjeni")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def updateDatum(_id, _datum):
        if not _id or not _datum or _id =='' or _datum == '' :
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"""UPDATE sesija SET datum_sesija= STR_TO_DATE('{_datum}','%d/%m/%Y %H:%i') where id = {_id}""")
            db.commit()
            alertWindow(f"Podaci uspjesno izmjenjeni")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    updateSesijaWin = Tk()
    updateSesijaWin.title("Update sesija")
    updateSesijaWin.geometry("250x500")

    tlabel = Label(updateSesijaWin, text=f"ID Sesije", bg="white")
    tlabel.grid(row=0, column=0)
    id_entry = Entry(updateSesijaWin)
    id_entry.grid(row=0, column=1)

    label_tim1 = Label(updateSesijaWin, text="Novo ID tima 1")
    label_tim1.grid(row=1, column=0)

    entry_tim1 = Entry(updateSesijaWin)
    entry_tim1.grid(row=1, column=1)

    mjenjajtim1 = Button(updateSesijaWin, text="Update tim1", command=lambda: updatetim1(id_entry.get(), entry_tim1.get()))
    mjenjajtim1.grid(row=2, column=1, columnspan=2)###
    ##

    label_tim2 = Label(updateSesijaWin, text="Novo ID tima 2")
    label_tim2.grid(row=3, column=0)

    entry_tim2 = Entry(updateSesijaWin)
    entry_tim2.grid(row=3, column=1)

    mjenjajtim2 = Button(updateSesijaWin, text="Update tim2", command=lambda: updatetim2(id_entry.get(), entry_tim2.get()))
    mjenjajtim2.grid(row=4, column=1, columnspan=2)

####
    label_sudac = Label(updateSesijaWin, text="Novi ID suca")
    label_sudac.grid(row=5, column=0)

    entry_sudac = Entry(updateSesijaWin)
    entry_sudac.grid(row=5, column=1)

    mjenjajsudac = Button(updateSesijaWin, text="Update sudac", command=lambda: updateSudac(id_entry.get(), entry_sudac.get()))
    mjenjajsudac.grid(row=6, column=1, columnspan=2)

    ###

    label_stadion = Label(updateSesijaWin, text="Novi ID stadiona ")
    label_stadion.grid(row=7, column=0)

    entry_stadion = Entry(updateSesijaWin)
    entry_stadion.grid(row=7, column=1)

    mjenjajstadion = Button(updateSesijaWin, text="Update stadion", command=lambda: updateStadion(id_entry.get(), entry_stadion.get()))
    mjenjajstadion.grid(row=8, column=1, columnspan=2)

    ###

    label_datum = Label(updateSesijaWin, text="Novi datum: d/m/Y H:m ")
    label_datum.grid(row=9, column=0)

    entry_datum = Entry(updateSesijaWin)
    entry_datum.grid(row=9, column=1)

    mjenjajdatum = Button(updateSesijaWin, text="Update datum",  command=lambda: updateDatum(id_entry.get(), entry_datum.get()))
    mjenjajdatum.grid(row=10, column=1, columnspan=2)