
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


#dohvaca sve igrace i ispisuje ih na zaseban prozor
def pokaziIgrace():
    igraci = Tk()
    igraci.title("Lista igraca")
    igraci.geometry("250x500")

    cursor.execute("SELECT * FROM igrac")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(igraci, text=f"[ID:{rezultat[0]}]. {rezultat[1]} | {rezultat[2]} | {rezultat[3]} | {rezultat[4]} | {rezultat[5]}", bg="white")
        test_label.pack()


# dodaje igraca koji puni korisnik sucelja custom podacima
def dodajIgrace():

    def igracToDb(ime, prezime, datum_rodenja, grad, tim):
        try:
            if not datum_rodenja or datum_rodenja == '':
                alertWindow('Trebate upisati datum rodenja')
                return
            
            cursor.execute(f"""INSERT INTO igrac(ime,prezime,datum_rodenja, id_grad, id_tim) 
                                    VALUES("{ime}","{prezime}",str_to_date('{datum_rodenja}','%d/%m/%Y'), {grad}, {tim})""")
            db.commit()
            clear()
            alertWindow(f'Uspješno dodan "{ime} {prezime}" u bazu podataka')
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')
            return

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

    dodaj_igraca = Tk()
    dodaj_igraca.title("Dodaj igraca")
    dodaj_igraca.geometry("250x800")

    label_ime = Label(dodaj_igraca, text="Ime")
    label_ime.grid(row=0, column=0)

    label_prezime = Label(dodaj_igraca, text="Prezime")
    label_prezime.grid(row=1, column=0)

    label_dr = Label(dodaj_igraca, text="Datum_rodenja\n(dd/mm/yyyy)")
    label_dr.grid(row=2, column=0)


    label_grad = Label(dodaj_igraca, text="Grad")
    label_grad.grid(row=3, column=0)

    label_tim = Label(dodaj_igraca, text="Tim")
    label_tim.grid(row=4, column=0)

    entry_ime = Entry(dodaj_igraca)
    entry_ime.grid(row= 0, column=1)

    entry_prezime = Entry(dodaj_igraca)
    entry_prezime.grid(row=1, column=1)

    entry_dr = Entry(dodaj_igraca)
    entry_dr.grid(row=2, column=1)

    lista_gradova = Listbox(dodaj_igraca, exportselection=0)
    lista_gradova.grid(row=3, column=1)

    lista_timova = Listbox(dodaj_igraca, exportselection=0)
    lista_timova.grid(row=4, column=1)

    popuniGradIzbor(lista_gradova)
    popuniTimoveIzbor(lista_timova)

    dodajIgraca_gumb = Button(dodaj_igraca, text="Dodaj", command=lambda:igracToDb(entry_ime.get(),entry_prezime.get(), entry_dr.get(), getGradIDFromName(), dobiIDtima()))
    dodajIgraca_gumb.grid(row=6, column=1, columnspan=2)


# brise igraca iz baze
def deleteIgracEntry():

    def deleteIgrac():
        try:
            izbor = lista_igraca.get(lista_igraca.curselection())
            izbor_p = getIDnumFromString(izbor)
            cursor.execute(f"DELETE FROM igrac WHERE id = '{izbor_p}'")
            db.commit()
            alertWindow(f"Igrac [ID:{izbor_p}] uspjesno izbrisan!")
        except Exception as e:
            alertWindow(f'Došlo je do greške [{e}]')

    def getIDnumFromString(string):
        num = int(''.join(filter(str.isdigit, f'{string}')))
        return num

    deleteIgracWin = Tk()
    deleteIgracWin.title("Brisanje Igraca")
    deleteIgracWin.geometry("250x250")

    cursor.execute("SELECT * FROM igrac")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o igracima
    lista_igraca = Listbox(deleteIgracWin, exportselection=0)
    lista_igraca.pack()

    # puni se selekcija za brisanje igraca
    for x in rezultati:
        lista_igraca.insert(END, f"ID:[{x[0]}] {x[1]} {x[2]}")

    brisiGumb = Button(deleteIgracWin, text="Izbrisi", pady=5, command=deleteIgrac)
    brisiGumb.pack()