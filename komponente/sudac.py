
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


def updatesudac():

    def updatesudacImeFunc(_id, _ime):

        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return

        try:
            cursor.execute(f"UPDATE sudac SET ime = '{_ime}' WHERE id = {_id};")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updatesudacPrezimeFunc(_id, _ime):

        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return

        try:
            cursor.execute(f"UPDATE sudac SET ime = '{_ime}' WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updatesudacDatumRodenjaFunc(_id, _datum):

        if not _id or not _datum or _id == '' or _datum == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return

        try:
            cursor.execute(f"UPDATE sudac SET datum_rodenja = str_to_date('{_datum}','%d/%m/%Y') WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    def updateGradImeFunc(_id, _ime):
        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return
        try:
            cursor.execute(f"UPDATE sudac SET id_grad = (SELECT id FROM grad WHERE ime = '{_ime}') WHERE id = {_id}")
            db.commit()
            alertWindow('Uspješna izmjena!')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')


    updatesudacWin = Tk()
    updatesudacWin.title("Update sudac")
    updatesudacWin.geometry("250x300")

    label_id = Label(updatesudacWin, text="ID sudca: ")
    label_id.grid(row=0, column=0)

    entry_idsudaca = Entry(updatesudacWin)
    entry_idsudaca.grid(row=0, column=1)

    label_ime = Label(updatesudacWin, text="Novo ime sudca: ")
    label_ime.grid(row=1, column=0)

    entry_ime = Entry(updatesudacWin)
    entry_ime.grid(row=1, column=1)

    updejtajImeGumb = Button(updatesudacWin, text="Update ime sudaca", command=lambda: updatesudacImeFunc(entry_idsudaca.get(), entry_ime.get()))
    updejtajImeGumb.grid(row=2, column=1, columnspan=2)

############

    label_prezime = Label(updatesudacWin, text = 'Novo prezime sudca :')
    label_prezime.grid(row=3, column=0)

    entry_prezime = Entry(updatesudacWin)
    entry_prezime.grid(row=3, column=1)

    updejtajPrezimeGumb = Button(updatesudacWin, text="Update prezime sudca", command=lambda: updatesudacPrezimeFunc(entry_idsudaca.get(), entry_prezime.get()))
    updejtajPrezimeGumb.grid(row=4, column=1, columnspan=2)

############

    label_datum = Label(updatesudacWin, text='Datum_rodenja\n(dd/mm/yyyy)')
    label_datum.grid(row=5, column=0)

    entry_datum = Entry(updatesudacWin)
    entry_datum.grid(row=5, column=1)

    updejtajDatumGumb = Button(updatesudacWin, text="Update datum rodenja sudca", command=lambda: updatesudacDatumRodenjaFunc(entry_idsudaca.get(), entry_datum.get()))
    updejtajDatumGumb.grid(row=6, column=1, columnspan=2)


############

    label_grad = Label(updatesudacWin, text='Ime novog grada: ')
    label_grad.grid(row=7, column=0)

    entry_grad = Entry(updatesudacWin)
    entry_grad.grid(row=7, column=1)

    updejtajGradGumb = Button(updatesudacWin, text="Update grad sudaca", command=lambda: updateGradImeFunc(entry_idsudaca.get(), entry_grad.get()))
    updejtajGradGumb.grid(row=8, column=1, columnspan=2)



#dohvaca sve sudce i ispisuje ih na zaseban prozor
def pokaziSudce():
    prikaziSudce = Tk()
    prikaziSudce.title("Lista sudaca")
    prikaziSudce.geometry("250x500")

    cursor.execute("SELECT * FROM sudac")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(prikaziSudce, text=f"[ID:{rezultat[0]}] {rezultat[1]} | {rezultat[2]} | {rezultat[3]} | {rezultat[4]}", bg="white")
        test_label.pack()


# dodaje sudca koji puni korisnik sucelja custom podacima
def dodajSudca():

    def sudacToDb(ime, prezime, datum_rodenja,grad):
        try:
            if not datum_rodenja or datum_rodenja == '':
                alertWindow('Potreno je upisati datum rodenja')
                return

            cursor.execute(f"""INSERT INTO sudac(ime,prezime,datum_rodenja, id_grad) 
                                    VALUES("{ime}","{prezime}",str_to_date('{datum_rodenja}','%d/%m/%Y'), {grad})""")
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

    def getGradIDFromName():
        izbor = lista_gradova.get(lista_gradova.curselection())
        cursor.execute(f"SELECT * FROM grad WHERE ime = '{izbor}'")
        id = cursor.fetchone()
        return id[0]

    dodajSudac = Tk()
    dodajSudac.title("Dodaj sudca")
    dodajSudac.geometry("250x500")

    label_ime = Label(dodajSudac, text="Ime")
    label_ime.grid(row=0, column=0)

    label_prezime = Label(dodajSudac, text="Prezime")
    label_prezime.grid(row=1, column=0)

    label_dr = Label(dodajSudac, text="Datum_rodenja\n(dd/mm/yyyy)")
    label_dr.grid(row=2, column=0)


    label_grad = Label(dodajSudac, text="Grad")
    label_grad.grid(row=3, column=0)


    entry_ime = Entry(dodajSudac)
    entry_ime.grid(row= 0, column=1)

    entry_prezime = Entry(dodajSudac)
    entry_prezime.grid(row=1, column=1)

    entry_dr = Entry(dodajSudac)
    entry_dr.grid(row=2, column=1)

    lista_gradova = Listbox(dodajSudac, exportselection=0)
    lista_gradova.grid(row=3, column=1)

    popuniGradIzbor(lista_gradova)

    dodajSudca_gumb = Button(dodajSudac, text="Dodaj", command=lambda:sudacToDb(entry_ime.get(),entry_prezime.get(), entry_dr.get(), getGradIDFromName()))
    dodajSudca_gumb.grid(row=5, column=1, columnspan=2)


# brise sudca iz baze
def deleteSudacEntry():

    def deleteSudac():
        try:
            izbor = lista_sudaca.get(lista_sudaca.curselection())
            izbor_p = getIDnumFromString(izbor)
            cursor.execute(f"DELETE FROM sudac WHERE id = '{izbor_p}'")
            db.commit()
            alertWindow(f"Sudac [ID:{izbor_p}] uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')
    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    deleteSudacWin = Tk()
    deleteSudacWin.title("Brisanje Sudaca")
    deleteSudacWin.geometry("250x250")

    cursor.execute("SELECT * FROM sudac")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o sudcima
    lista_sudaca = Listbox(deleteSudacWin, exportselection=0)
    lista_sudaca.pack()

    # puni se selekcija za brisanje sudaca
    for x in rezultati:
        lista_sudaca.insert(END, f"ID:[{x[0]}] {x[1]} {x[2]}")

    brisiGumb = Button(deleteSudacWin, text="Izbrisi", pady=5, command=deleteSudac)
    brisiGumb.pack()
