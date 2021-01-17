
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *



def dodajOut(sesija_id):
    dodajOut = Tk()
    dodajOut.title("Dodaj zapis o out-u")
    dodajOut.geometry("500x350")


    if not sesija_id or sesija_id == '':
        test_label3 = Label(dodajOut, text='Niste upisali sesiju!', bg="white")
        test_label3.grid(row=1, column=1)
        return

    cursor.execute(f"SELECT * FROM sesija WHERE id = {sesija_id}")
    rezultati = cursor.fetchone()

    label_id = Label(dodajOut, text=f"Dodaj zapis o out-evima za sesiju:  [ID:{sesija_id}]")
    label_id.grid(row=0, column=0)

    if not rezultati:
        print('TRUE')
        test_label2 = Label(dodajOut, text='Nema podataka za ovu sesiju!', bg="white")
        label_id.grid(row=1, column=0)
        return


    def outUDB(id_sesije, id_tim, id_igrac, broj_outova):
        cursor.execute(f"""INSERT INTO out_s(id_sesija, id_tim, id_igrac, broj_outova)
                                VALUES({id_sesije},{id_tim},{id_igrac},{broj_outova})""")
        db.commit()
        alertWindow(f"Outevi uspjesno dodani u bazu podataka!")


    def getTimIDFromIgracID(id_igrac):
        cursor.execute(f'SELECT id_tim FROM igrac WHERE id = {id_igrac}')
        rezultat = cursor.fetchone()
        return rezultat[0]

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    label_igraci = Label(dodajOut, text="Igraci: ")
    label_igraci.grid(row=2, column=0)

    lista_igraca = Listbox(dodajOut, exportselection=0, width=50 )
    lista_igraca.grid(row=2, column=1)

    label_outevi = Label(dodajOut, text="Broj outova: ")
    label_outevi.grid(row=3, column=0)

    entry_outevi = Entry(dodajOut)
    entry_outevi.grid(row=3, column=1)
########################################

    popuniIgraceIzbor(lista_igraca, sesija_id)

    dodajUdarce_gumb = Button(dodajOut, text="Dodaj zapis", command=lambda:outUDB(sesija_id, getTimIDFromIgracID(getIDnumFromString(lista_igraca.get(lista_igraca.curselection()))), getIDnumFromString(lista_igraca.get(lista_igraca.curselection())),entry_outevi.get()))
    dodajUdarce_gumb.grid(row=6, column=1, columnspan=2)

def prikaziSveOutovePoSesiji(sesija_id):

    prikaziOutove = Tk()
    prikaziOutove.title("Lista outova")
    prikaziOutove.geometry("350x500")

    cursor.execute(f"""

    SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', o.broj_outova FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
        JOIN out_s o ON i.id = o.id_igrac
		WHERE s.id = {sesija_id}
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', o.broj_outova FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
        JOIN out_s o ON i.id = o.id_igrac
		WHERE s.id = {sesija_id};

""")
    rezultati = cursor.fetchall()

    for index, rezultat in enumerate(rezultati):
        test_label = Label(prikaziOutove, text=f"{rezultat[1]} | {rezultat[2]} -> {rezultat[3]} ", bg="white")
        test_label.pack()



def deleteOuteviEntry(sesija_id):


    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    def getPlayerNameFromId(string):
        cursor2.execute('SELECT ')
        return num


    def deleteOutevi():
        full_string = lista_outova.get(lista_outova.curselection())
        izbor = getIDnumFromString(lista_outova.get(lista_outova.curselection()))
        cursor.execute(f"DELETE FROM out_s WHERE id_igrac = '{izbor}'")
        db.commit()
        alertWindow(f"Outovi igraca {full_string} uspjesno izbrisan!")

    deleteOutWin = Tk()
    deleteOutWin.title("Brisanje outeva")
    deleteOutWin.geometry("250x250")

    cursor.execute(f"SELECT i.id,CONCAT(i.ime, ' ', i.prezime ) FROM out_s JOIN igrac i ON i.id = id_igrac WHERE id_sesija = {sesija_id}")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o timovima
    lista_outova = Listbox(deleteOutWin, exportselection=0)
    lista_outova.pack()

    # puni se selekcija za brisanje timova
    for x in rezultati:
        lista_outova.insert(END, f"[ID{x[0]}] {x[1]}")

    brisiGumb = Button(deleteOutWin, text="Izbrisi outove", pady=5, command=deleteOutevi)
    brisiGumb.pack()