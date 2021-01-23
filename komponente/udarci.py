
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *

def updateUdarce():

    def updateUdarciUkupnoFunc(_id, _idIgraca, _brUkupno):
        if not _id or not _idIgraca or _id == '' or _idIgraca == '' or _brUkupno == '' or not _brUkupno:
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"UPDATE udarci SET ukupno = '{_brUkupno}' WHERE id_sesija = {_id} AND id_igrac = {_idIgraca}")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updateUdarciUOkvirFunc(_id, _idIgraca, _brUokvir):
        if not _id or not _idIgraca or _id == '' or _idIgraca == '' or _brUokvir == '' or not _brUokvir:
            alertWindow('Trebate upisati sve parametre')
            return
        try:
            cursor.execute(f"UPDATE udarci SET ukupno = '{_brUkupno}' WHERE id_sesija = {_id} AND id_igrac = {_idIgraca}")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    updateUdarceWin = Tk()
    updateUdarceWin.title("Update udarci")
    updateUdarceWin.geometry("250x300")

    label_id = Label(updateUdarceWin, text="ID sesije: ")
    label_id.grid(row=0, column=0)

    entry_idSesije = Entry(updateUdarceWin)
    entry_idSesije.grid(row=0, column=1)

    label_idIgraca = Label(updateUdarceWin, text="ID igrača: ")
    label_idIgraca.grid(row=1, column=0)

    entry_idIgraca = Entry(updateUdarceWin)
    entry_idIgraca.grid(row=1, column=1)

    label_brOut = Label(updateUdarceWin, text="Novi broj ukupno: ")
    label_brOut.grid(row=2, column=0)

    entry_brOut = Entry(updateUdarceWin)
    entry_brOut.grid(row=2, column=1)

    updejtajUdarceGumb = Button(updateUdarceWin, text="Update ukupno", command=lambda: updateUdarce(entry_idSesije.get(), entry_idIgraca.get(), entry_brOut.get()))
    updejtajUdarceGumb.grid(row=3, column=1, columnspan=2)

    label_brOutss = Label(updateUdarceWin, text="Novi broj u okvir: ")
    label_brOutss.grid(row=4, column=0)

    entry_brOutss = Entry(updateUdarceWin)
    entry_brOutss.grid(row=4, column=1)

    updejtajUdarceOkGumb = Button(updateUdarceWin, text="Update u okvir",command=lambda: updateUdarciUOkvirFunc(entry_idSesije.get(), entry_idIgraca.get(), entry_brOutss.get()))
    updejtajUdarceOkGumb.grid(row=5, column=1, columnspan=2)


#####

def dodajUdarce(sesija_id):
    dodaj_udarce = Tk()
    dodaj_udarce.title("Dodaj zapis o udarcima")
    dodaj_udarce.geometry("500x350")


    if not sesija_id or sesija_id == '':
        test_label3 = Label(dodaj_udarce, text='Niste upisali sesiju!', bg="white")
        test_label3.grid(row=1, column=1)
        return

    cursor.execute(f"SELECT * FROM sesija WHERE id = {sesija_id}")
    rezultati = cursor.fetchone()

    label_id = Label(dodaj_udarce, text=f"Dodaj udarce za sesiju:  [ID:{sesija_id}]")
    label_id.grid(row=0, column=0)

    if not rezultati:
        print('TRUE')
        test_label2 = Label(dodaj_udarce, text='Nema podataka za ovu sesiju!', bg="white")
        label_id.grid(row=1, column=0)
        return


    def udarciUdb(id_sesije, id_tim, id_igrac, ukupno, u_okvir):
        try:
            cursor.execute(f"""INSERT INTO udarci(id_sesija, id_tim, id_igrac, ukupno, u_okvir) 
                                    VALUES({id_sesije},{id_tim},{id_igrac},{ukupno},{u_okvir})""")
            db.commit()
            alertWindow(f"Udarci uspjesno dodani u bazu podataka!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def getTimIDFromIgracID(id_igrac):
        cursor.execute(f'SELECT id_tim FROM igrac WHERE id = {id_igrac}')
        rezultat = cursor.fetchone()
        return rezultat[0]

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    label_igraci = Label(dodaj_udarce, text="Igraci: ")
    label_igraci.grid(row=2, column=0)

    lista_igraca = Listbox(dodaj_udarce, exportselection=0, width=50 )
    lista_igraca.grid(row=2, column=1)

    label_ukupno = Label(dodaj_udarce, text="Ukupno: ")
    label_ukupno.grid(row=3, column=0)

    entry_ukupno = Entry(dodaj_udarce)
    entry_ukupno.grid(row=3, column=1)
########################################

    label_uOkvir = Label(dodaj_udarce, text="U okvir: ")
    label_uOkvir.grid(row=4, column=0)

    entry_uOkvir = Entry(dodaj_udarce)
    entry_uOkvir.grid(row=4, column=1)


    popuniIgraceIzbor(lista_igraca, sesija_id)

    dodajUdarce_gumb = Button(dodaj_udarce, text="Dodaj zapis", command=lambda: udarciUdb(sesija_id, getTimIDFromIgracID(getIDnumFromString(lista_igraca.get(lista_igraca.curselection()))), getIDnumFromString(lista_igraca.get(lista_igraca.curselection())),entry_ukupno.get(),entry_uOkvir.get()))
    dodajUdarce_gumb.grid(row=6, column=1, columnspan=2)

def prikaziSveUdarcePoSesiji(sesija_id):

    prikaziUdarce = Tk()
    prikaziUdarce.title("Lista udaraca")
    prikaziUdarce.geometry("350x500")

    cursor.execute(f""" 

    SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', u.ukupno, u.u_okvir FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
        JOIN udarci u ON i.id = u.id_igrac
		WHERE s.id = {sesija_id}
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', u.ukupno, u.u_okvir FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
        JOIN udarci u ON i.id = u.id_igrac
		WHERE s.id = {sesija_id};

""")
    rezultati = cursor.fetchall()

    for index, rezultat in enumerate(rezultati):
        test_label = Label(prikaziUdarce, text=f"{rezultat[1]} | {rezultat[2]} -> UKUPNO: {rezultat[3]} || U OKVIR: {rezultat[4]}", bg="white")
        test_label.pack()



def deleteUdaracEntry(sesija_id):


    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    def getPlayerNameFromId(string):
        cursor2.execute('SELECT ')
        return num


    def deleteUdarac():
        full_string = lista_udaraca.get(lista_udaraca.curselection())
        izbor = getIDnumFromString(lista_udaraca.get(lista_udaraca.curselection()))
        cursor.execute(f"DELETE FROM udarci WHERE id_igrac = '{izbor}'")
        db.commit()
        alertWindow(f"Udarci igraca {full_string} uspjesno izbrisan!")

    deleteUdarciWin = Tk()
    deleteUdarciWin.title("Brisanje udaraca")
    deleteUdarciWin.geometry("250x250")

    cursor.execute(f"SELECT i.id,CONCAT(i.ime, ' ', i.prezime ) FROM udarci JOIN igrac i ON i.id = id_igrac WHERE id_sesija = {sesija_id}")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o timovima
    lista_udaraca = Listbox(deleteUdarciWin, exportselection=0)
    lista_udaraca.pack()

    # puni se selekcija za brisanje timova
    for x in rezultati:
        lista_udaraca.insert(END, f"[ID{x[0]}] {x[1]}")

    brisiGumb = Button(deleteUdarciWin, text="Izbrisi udarce", pady=5, command=deleteUdarac)
    brisiGumb.pack()