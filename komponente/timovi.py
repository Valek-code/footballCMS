
from tkinter import *
from tkinter import ttk
import mysql.connector
from komponente import selekcije
from komponente.selekcije import *
from komponente.sqlConnection import *



#dohvaca sve timove i ispisuje ih na zaseban prozor
def showTeams():
    prikaziTim = Tk()
    prikaziTim.title("Lista timova")
    prikaziTim.geometry("250x500")

    cursor.execute("SELECT * FROM tim")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(prikaziTim, text=f"{rezultat[0]}. {rezultat[1]} | {rezultat[2]}", bg="white")
        test_label.pack()


# brise tim iz baze
def deleteTeamEntry():

    def deleteTeam():
        izbor = lista_timova.get(lista_timova.curselection())
        cursor.execute(f"DELETE FROM tim WHERE ime = '{izbor}'")
        db.commit()
        alertWindow(f"Tim {izbor} uspjesno izbrisan!")

    deleteTeamWin = Tk()
    deleteTeamWin.title("Brisanje Tima")
    deleteTeamWin.geometry("250x250")

    cursor.execute("SELECT * FROM tim")
    rezultati = cursor.fetchall()

    # generiranje liste koja cuva podatke o timovima
    lista_timova = Listbox(deleteTeamWin, exportselection=0)
    lista_timova.pack()

    # puni se selekcija za brisanje timova
    for x in rezultati:
        lista_timova.insert(END, f"{x[1]}")

    brisiGumb = Button(deleteTeamWin, text="Izbrisi", pady=5, command=deleteTeam)
    brisiGumb.pack()





# dodaje Tim koji puni korisnik sucelja custom podacima
def dodajTim():

    def timToDb(ime, kratica, drzava, grad):
        cursor.execute(f"""INSERT INTO tim(ime,kratica,id_drzava,id_grad) 
                                VALUES("{ime}","{kratica}",{drzava},{grad})""")
        db.commit()
        clear()

    def clear():
        entry_ime.delete(0, END)
        entry_kratica.delete(0, END)
        lista_gradova.selection_clear(0, END)
        lista_drzava.selection_clear(0, END)

    dodajTim = Tk()
    dodajTim.title("Dodaj tim")
    dodajTim.geometry("250x500")

    label_ime = Label(dodajTim, text="Ime tima")
    label_ime.grid(row=0, column=0)

    label_kratica = Label(dodajTim, text="Kratica")
    label_kratica.grid(row=1, column=0)

    label_drzava = Label(dodajTim, text="Drzava")
    label_drzava.grid(row=2, column=0)

    label_grad = Label(dodajTim, text="Grad")
    label_grad.grid(row=3, column=0)


    entry_ime = Entry(dodajTim)
    entry_ime.grid(row= 0, column=1)

    entry_kratica = Entry(dodajTim)
    entry_kratica.grid(row=1, column=1)

    lista_drzava = Listbox(dodajTim, exportselection=0)
    lista_drzava.grid(row=2, column=1)

    lista_gradova = Listbox(dodajTim, exportselection=0)
    lista_gradova.grid(row=3, column=1)

    popuniDrzaveIzbor(lista_drzava)
    popuniGradIzbor(lista_gradova)

    dodajTim_gumb = Button(dodajTim, text="Dodaj", command=lambda:timToDb(entry_ime.get(),entry_kratica.get(), lista_drzava.curselection()[0]+1, lista_gradova.curselection()[0]+1))
    dodajTim_gumb.grid(row=4, column=1, columnspan=2)

