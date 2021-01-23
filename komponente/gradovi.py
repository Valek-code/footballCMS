
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


def updateGrad():

    def updateGradImeFunc(_id, _ime):
        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return
        try:
            cursor.execute(f"UPDATE grad SET ime = '{_ime}' WHERE id = {_id}")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')

    def updateDrzavaImeFunc(_id, _ime):
        if not _id or not _ime or _id == '' or _ime == '':
            alertWindow('Trebate upisati sve parametre ili id nije upisan')
            return
        try:
            cursor.execute(f"UPDATE grad SET id_drzava = (SELECT id FROM drzava WHERE ime = '{_ime}') WHERE id = {_id}")
            db.commit()
            alertWindow(f'Uspješno izmjenjeno.')
        except Exception as e:
            alertWindow(f'Došlo je do greške {e}')

    updateGradWin = Tk()
    updateGradWin.title("Update grad")
    updateGradWin.geometry("250x300")

    label_id = Label(updateGradWin, text="ID grada: ")
    label_id.grid(row=0, column=0)

    entry_idGrada = Entry(updateGradWin)
    entry_idGrada.grid(row=0, column=1)

    label_ime = Label(updateGradWin, text="Novo ime grada: ")
    label_ime.grid(row=1, column=0)

    entry_ime = Entry(updateGradWin)
    entry_ime.grid(row=1, column=1)

    updejtajGradGumb = Button(updateGradWin, text="Update ime grada", command=lambda: updateGradImeFunc(entry_idGrada.get(), entry_ime.get()))
    updejtajGradGumb.grid(row=2, column=1, columnspan=2)

    label_ime_drzave = Label(updateGradWin, text = 'Ime države :')
    label_ime_drzave.grid(row=3, column=0)

    entry_ime_drzave = Entry(updateGradWin)
    entry_ime_drzave.grid(row=3, column=1)

    updejtajDrzavuGumb = Button(updateGradWin, text="Update drzavu grada", command=lambda: updateDrzavaImeFunc(entry_idGrada.get(), entry_ime_drzave.get()))
    updejtajDrzavuGumb.grid(row=4, column=1, columnspan=2)


#dohvaca sve sudce i ispisuje ih na zaseban prozor
def pokaziGradove():
    prikaziGradove = Tk()
    prikaziGradove.title("Lista gradova")
    prikaziGradove.geometry("250x500")

    cursor.execute("SELECT * FROM grad")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):
        cursor2.execute(f'SELECT ime FROM drzava WHERE id = {rezultat[2]}')
        drzRez = cursor2.fetchone()
        test_label = Label(prikaziGradove, text=f"[ID:{rezultat[0]}]. {rezultat[1]} => {drzRez[0]}", bg="white")
        test_label.pack()


# dodaje sudca koji puni korisnik sucelja custom podacima
def dodajGradove():

    def gradToDb(ime):
        try:
            cursor.execute(f"""INSERT INTO grad(ime, id_drzava) 
                                    VALUES("{ime}")""")
            db.commit()
            clear()
            alertWindow(f"Grad {ime} uspjesno dodan u bazu podataka!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def clear():
        entry_ime.delete(0, END)

    dodajGrad = Tk()
    dodajGrad.title("Dodaj grad")
    dodajGrad.geometry("250x500")

    label_ime = Label(dodajGrad, text="Ime")
    label_ime.grid(row=0, column=0)

    entry_ime = Entry(dodajGrad)
    entry_ime.grid(row= 0, column=1)

    label_drzava = Label(dodajGrad, text="Drzava")
    label_drzava.grid(row=1, column=0)

    lista_drzava = Listbox(dodajGrad, exportselection=0)
    lista_drzava.grid(row=1, column=1)


    dodajGradGumb = Button(dodajGrad, text="Dodaj", command=lambda:gradToDb(entry_ime.get()))
    dodajGradGumb.grid(row=5, column=1, columnspan=2)

    popuniDrzaveIzbor(lista_drzava)


def deleteGradEntry():

    def deleteGrad():

        try:
            izbor = lista_gradova.get(lista_gradova.curselection())
            cursor.execute(f"DELETE FROM grad WHERE ime = '{izbor}'")
            db.commit()
            alertWindow(f"Grad [ID:{izbor}] uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške: {e}')

    deleteGradWin = Tk()
    deleteGradWin.title("Brisanje gradova")
    deleteGradWin.geometry("250x250")

    cursor.execute("SELECT * FROM grad")
    rezultati = cursor.fetchall()


    lista_gradova = Listbox(deleteGradWin, exportselection=0)
    lista_gradova.pack()

    label_upozorenje = Label(deleteGradWin, text="Ne mozete brisati slucajeve \n koji su vec u opticaju")
    label_upozorenje.pack()

    for x in rezultati:
        lista_gradova.insert(END, f"{x[1]}")

    brisiGumb = Button(deleteGradWin, text="Izbrisi", pady=5, command=deleteGrad)
    brisiGumb.pack()
