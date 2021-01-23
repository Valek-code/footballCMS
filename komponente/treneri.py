
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


def updatetrener():

    def updatetrenerImeFunc(_id, _ime):

        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return

        try:
            cursor.execute(f"UPDATE trener SET ime = '{_ime}' WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updatetrenerPrezimeFunc(_id, _ime):

        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return

        try:
            cursor.execute(f"UPDATE trener SET ime = '{_ime}' WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updatetrenerDatumRodenjaFunc(_id, _datum):

        if not _id or not _datum or _id == '' or _datum == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return

        try:
            cursor.execute(f"UPDATE trener SET datum_rodenja = str_to_date('{_datum}','%d/%m/%Y') WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updateTimImeFunc(_id, _ime):
        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return
        try:
            cursor.execute(f"UPDATE trener SET id_tim = (SELECT id FROM tim WHERE ime = '{_ime}') WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updateGradImeFunc(_id, _ime):
        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return
        try:
            cursor.execute(f"UPDATE trener SET id_grad = (SELECT id FROM grad WHERE ime = '{_ime}') WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    updatetrenerWin = Tk()
    updatetrenerWin.title("Update treneri")
    updatetrenerWin.geometry("250x300")

    label_id = Label(updatetrenerWin, text="ID trenera: ")
    label_id.grid(row=0, column=0)

    entry_idtrenera = Entry(updatetrenerWin)
    entry_idtrenera.grid(row=0, column=1)

    label_ime = Label(updatetrenerWin, text="Novo ime trenera: ")
    label_ime.grid(row=1, column=0)

    entry_ime = Entry(updatetrenerWin)
    entry_ime.grid(row=1, column=1)

    updejtajImeGumb = Button(updatetrenerWin, text="Update ime trenera", command=lambda: updatetrenerImeFunc(entry_idtrenera.get(), entry_ime.get()))
    updejtajImeGumb.grid(row=2, column=1, columnspan=2)

############

    label_prezime = Label(updatetrenerWin, text = 'Novo prezime trenera :')
    label_prezime.grid(row=3, column=0)

    entry_prezime = Entry(updatetrenerWin)
    entry_prezime.grid(row=3, column=1)

    updejtajPrezimeGumb = Button(updatetrenerWin, text="Update prezime trenera", command=lambda: updatetrenerPrezimeFunc(entry_idtrenera.get(), entry_prezime.get()))
    updejtajPrezimeGumb.grid(row=4, column=1, columnspan=2)

############

    label_datum = Label(updatetrenerWin, text='Datum_rodenja\n(dd/mm/yyyy)')
    label_datum.grid(row=5, column=0)

    entry_datum = Entry(updatetrenerWin)
    entry_datum.grid(row=5, column=1)

    updejtajDatumGumb = Button(updatetrenerWin, text="Update datum rodenja trenera", command=lambda: updatetrenerDatumRodenjaFunc(entry_idtrenera.get(), entry_datum.get()))
    updejtajDatumGumb.grid(row=6, column=1, columnspan=2)


############

    label_grad = Label(updatetrenerWin, text='Ime novog grada: ')
    label_grad.grid(row=7, column=0)

    entry_grad = Entry(updatetrenerWin)
    entry_grad.grid(row=7, column=1)

    updejtajGradGumb = Button(updatetrenerWin, text="Update grad trenera", command=lambda: updateGradImeFunc(entry_idtrenera.get(), entry_grad.get()))
    updejtajGradGumb.grid(row=8, column=1, columnspan=2)

############

    label_tim = Label(updatetrenerWin, text='Ime novog tima: ')
    label_tim.grid(row=9, column=0)

    entry_tim = Entry(updatetrenerWin)
    entry_tim.grid(row=9, column=1)

    updejtajTimGumb = Button(updatetrenerWin, text="Update datum rodenja trenera", command=lambda: updateTimImeFunc(entry_idtrenera.get(), entry_tim.get()))
    updejtajTimGumb.grid(row=10, column=1, columnspan=2)



#dohvaca sve trenere i ispisuje ih na zaseban prozor
def pokaziTrenere():
    treneri = Tk()
    treneri.title("Lista trenera")
    treneri.geometry("250x500")

    cursor.execute("SELECT * FROM trener")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(treneri, text=f"[ID:{rezultat[0]}]. {rezultat[1]} | {rezultat[2]} | {rezultat[3]} | {rezultat[4]} | {rezultat[5]}", bg="white")
        test_label.pack()


# dodaje trenera koji puni korisnik sucelja custom podacima
def dodajTrenera():

    def trenerToDb(ime, prezime, datum_rodenja, grad, tim):
        try:
            if not datum_rodenja or datum_rodenja == '':
                alertWindow('Potrebno je upisati datum rodenja')
                return

            cursor.execute(f"""INSERT INTO trener(ime,prezime,datum_rodenja, id_grad, id_tim) 
                                    VALUES("{ime}","{prezime}",str_to_date('{datum_rodenja}','%d/%m/%Y'), {grad}, {tim})""")
            db.commit()
            clear()
            alertWindow(f'Uspješno dodan "{ime} {prezime}" u bazu podataka')
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')
    def clear():
        entry_ime.delete(0, END)
        entry_prezime.delete(0, END)
        entry_dr.delete(0,END)
        lista_gradova.selection_clear(0, END)
        lista_timova.selection_clear(0, END)

    def dobiIDtima():
        izbor = lista_timova.get(lista_timova.curselection())
        cursor.execute(f"SELECT * FROM tim WHERE ime = '{izbor}'")
        id = cursor.fetchone()
        return id[0]

    def getGradIDFromName():
        izbor = lista_gradova.get(lista_gradova.curselection())
        cursor.execute(f"SELECT * FROM grad WHERE ime = '{izbor}'")
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

    label_grad = Label(dodaj_trenera, text="Grad")
    label_grad.grid(row=3, column=0)

    label_tim = Label(dodaj_trenera, text="Tim")
    label_tim.grid(row=4, column=0)


    entry_ime = Entry(dodaj_trenera)
    entry_ime.grid(row= 0, column=1)

    entry_prezime = Entry(dodaj_trenera)
    entry_prezime.grid(row=1, column=1)

    entry_dr = Entry(dodaj_trenera)
    entry_dr.grid(row=2, column=1)


    lista_gradova = Listbox(dodaj_trenera, exportselection=0)
    lista_gradova.grid(row=3, column=1)

    lista_timova = Listbox(dodaj_trenera, exportselection=0)
    lista_timova.grid(row=4, column=1)

    popuniGradIzbor(lista_gradova)
    popuniTimoveIzbor(lista_timova)

    dodajSudca_gumb = Button(dodaj_trenera, text="Dodaj", command=lambda:trenerToDb(entry_ime.get(),entry_prezime.get(), entry_dr.get(), getGradIDFromName(), dobiIDtima()))
    dodajSudca_gumb.grid(row=6, column=1, columnspan=2)


# brise trenera iz baze
def deleteTrenerEntry():

    def deleteTrener():
        try:
            izbor = lista_trenera.get(lista_sudaca.curselection())
            izbor_p = getIDnumFromString(izbor)
            cursor.execute(f"DELETE FROM trener WHERE id = '{izbor}'")
            db.commit()
            alertWindow(f"Trener ID:[{izbor}] uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

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
        lista_trenera.insert(END, f"[ID:{x[0]}] {x[1]} {x[2]}")

    brisiGumb = Button(deleteSudacWin, text="Izbrisi", pady=5, command=deleteTrener)
    brisiGumb.pack()
