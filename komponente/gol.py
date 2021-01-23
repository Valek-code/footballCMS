
from tkinter import *
from tkinter import ttk
import mysql.connector
from datetime import datetime

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *

def updateGolove():
    updateGolWin = Tk()
    updateGolWin.title("Update golove")
    updateGolWin.geometry("250x300")


    def updateGoloviIgracFunc(_id, _vrijeme, _noviIdGraca, _idIgraca):

        if not _id or not _idIgraca or _id == '' or _idIgraca == '' or _noviIdGraca == '' or not _noviIdGraca:
            alertWindow('Trebate upisati sve parametre ili jedan od id-eva nije unesen')
            return
        try:
            cursor.execute(f"UPDATE gol SET id_igrac = {_noviIdGraca} WHERE id_sesija = {_id} AND id_igrac = {_idIgraca} AND vrijeme = str_to_date('{_vrijeme}','%d/%m/%Y %H:%i')")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updateGoloviVrijemeFunc(_id, _vrijeme,_novoVrijeme, _idIgraca):
        if not _id or not _idIgraca or _id == '' or _idIgraca == '' or not _novoVrijeme or _novoVrijeme == '':
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"UPDATE gol SET vrijeme = str_to_date('{_novoVrijeme}','%d/%m/%Y %H:%i') WHERE id_sesija = {_id} AND id_igrac = {_idIgraca} AND vrijeme = str_to_date('{_vrijeme}','%d/%m/%Y %H:%i')")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    label_id_sesija = Label(updateGolWin, text="ID sesije: ")
    label_id_sesija.grid(row=0, column=0)

    entry_id_sesija = Entry(updateGolWin)
    entry_id_sesija.grid(row=0, column=1)


    label_id_igrac = Label(updateGolWin, text="ID igrača: ")
    label_id_igrac.grid(row=1, column=0)

    entry_id_igrac = Entry(updateGolWin)
    entry_id_igrac.grid(row=1, column=1)


    label_id_vrijeme = Label(updateGolWin, text="Vrijeme\ndd/mm/YYYY H:MIN:")
    label_id_vrijeme.grid(row=2, column=0)

    entry_vrijeme = Entry(updateGolWin)
    entry_vrijeme.grid(row=2, column=1)


    label_id_novi_igrac = Label(updateGolWin, text="ID novog igraca: ")
    label_id_novi_igrac.grid(row=3, column=0)

    entry_id_novi_igrac = Entry(updateGolWin)
    entry_id_novi_igrac.grid(row=3, column = 1)

    updejtGoloviGumb = Button(updateGolWin, text="Update novi igrac", command=lambda:updateGoloviIgracFunc(entry_id_sesija.get(), entry_vrijeme.get(), entry_id_novi_igrac.get(), entry_id_igrac.get()))
    updejtGoloviGumb.grid(row=4, column = 1, columnspan=2)

    label_id_novo_vrijeme = Label(updateGolWin, text="Vrijeme(novo)\ndd/mm/YYYY H:MIN:")
    label_id_novo_vrijeme.grid( row=5, column=0 )

    entry_id_novo_vrijeme = Entry(updateGolWin)
    entry_id_novo_vrijeme.grid( row=5, column = 1 )

    updejtGoloviGumb = Button(updateGolWin, text="Update novo vrijeme",command=lambda: updateGoloviIgracFunc(entry_id_sesija.get(), entry_vrijeme.get(),entry_id_novo_vrijeme.get(), entry_id_igrac.get()))
    updejtGoloviGumb.grid(row=6, column=1, columnspan=2)


def dodajGolove(sesija_id):
    dodaj_gol = Tk()
    dodaj_gol.title("Dodaj gol sesiji")
    dodaj_gol.geometry("500x250")


    if not sesija_id or sesija_id == '':
        test_label3 = Label(dodaj_gol, text='Niste upisali sesiju!', bg="white")
        test_label3.grid(row=1, column=1)
        return

    cursor.execute(f"SELECT * FROM sesija WHERE id = {sesija_id}")
    rezultati = cursor.fetchone()

    label_id = Label(dodaj_gol, text=f"Dodaj golove za sesiju:  [ID:{sesija_id}]")
    label_id.grid(row=0, column=0)

    if not rezultati:
        print('TRUE')
        test_label2 = Label(dodaj_gol, text='Nema podataka za ovu sesiju!', bg="white")
        label_id.grid(row=1, column=0)
        return


    def golToDb(id_sesije, id_tim, id_igrac, vrijeme):

        try:
            if not vrijeme or vrijeme == '':
                alertWindow('Morate upisati vrijeme gola')
                return

            cursor.execute(f"""INSERT INTO gol(id_sesija, id_tim, id_igrac, vrijeme) 
                                            VALUES({id_sesije},{id_tim},{id_igrac}, STR_TO_DATE('{vrijeme}','%d/%m/%Y %H:%i'))""")
            db.commit()
            alertWindow(f"Gol uspjesno dodan u bazu podataka!")
        except Exception as e:
            alertWindow(f'Došlo je do greškess [{e}]')


    def getTimIDFromIgracID(id_igrac):
        cursor.execute(f'SELECT id_tim FROM igrac WHERE id = {id_igrac}')
        rezultat = cursor.fetchone()
        return rezultat[0]

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num


    label_igraci = Label(dodaj_gol, text="Igraci: ")
    label_igraci.grid(row=2, column=0)

    lista_igraca = Listbox(dodaj_gol, exportselection=0, width=50 )
    lista_igraca.grid(row=2, column=1)

    label_vrijeme = Label(dodaj_gol, text="Vrijeme gola(dd/mm/yyyy HH:MIN):")
    label_vrijeme.grid(row=3, column=0)

    entry_vrijeme = Entry(dodaj_gol)
    entry_vrijeme.grid(row=3, column=1)


    popuniIgraceIzbor(lista_igraca, sesija_id)

    dodajGol_gumb = Button(dodaj_gol, text="Dodaj gol", command=lambda: golToDb(sesija_id, getTimIDFromIgracID(getIDnumFromString(lista_igraca.get(lista_igraca.curselection()))), getIDnumFromString(lista_igraca.get(lista_igraca.curselection())),entry_vrijeme.get()))
    dodajGol_gumb.grid(row=4, column=1, columnspan=2)

def prikaziSveGolovePoSesiji(sesija_id):

    prikaziGol = Tk()
    prikaziGol.title("Lista golova")
    prikaziGol.geometry("350x500")

    cursor.execute(f""" 

    SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', g.vrijeme FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
        JOIN gol g ON i.id = g.id_igrac
		WHERE s.id = {sesija_id}
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', g.vrijeme FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
        JOIN gol g ON i.id = g.id_igrac
		WHERE s.id = {sesija_id};

""")
    rezultati = cursor.fetchall()

    for index, rezultat in enumerate(rezultati):
        test_label = Label(prikaziGol, text=f"{rezultat[1]} | {rezultat[2]} -> {rezultat[3]}", bg="white")
        test_label.pack()



def deleteGolEntry(sesija_id):

    def deleteGol():
        try:
            izbor = lista_golova.get(lista_golova.curselection())
            cursor.execute(f"DELETE FROM gol WHERE vrijeme = '{izbor}'")
            db.commit()
            alertWindow(f"Gol [TIMESTAMP:{izbor}] uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    deleteGoalWin = Tk()
    deleteGoalWin.title("Brisanje golova")
    deleteGoalWin.geometry("250x250")

    cursor.execute(f"SELECT * FROM gol WHERE id_sesija = {sesija_id}")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o timovima
    lista_golova = Listbox(deleteGoalWin, exportselection=0)
    lista_golova.pack()

    # puni se selekcija za brisanje timova
    for x in rezultati:
        lista_golova.insert(END, f"{x[3]}")

    brisiGumb = Button(deleteGoalWin, text="Izbrisi gol", pady=5, command=deleteGol)
    brisiGumb.pack()