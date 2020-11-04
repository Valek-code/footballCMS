from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import csv



db = mysql.connector.connect(
    host="localhost",
    user="user",
    auth_plugin='mysql_native_password',
    passwd="lozinka(upisi_svoju_lol)",
    db="projekt"
)

cursor = db.cursor()


def popuniGradIzbor(lista):
    cursor.execute("SELECT * FROM grad")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[1]}")

def popuniDrzaveIzbor(lista):
    cursor.execute("SELECT * FROM drzava")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[1]}")

def getTimovi():
    cursor.execute("SELECT * FROM tim")
    rezultati = cursor.fetchall()

    for index,rezultat in enumerate(rezultati):

        test_label = Label(frame5, text=f"{rezultat[0]}. {rezultat[1]} | {rezultat[2]}", bg="white")
        test_label.pack()

def refreshTim():
    cursor.execute("SELECT * FROM tim")
    rezultati = cursor.fetchall()


def dodajTim():


    def timToDb(ime, kratica, drzava, grad):
        cursor.execute(f"""INSERT INTO tim(ime,kratica,id_drzava,id_grad) 
                                VALUES("{ime}","{kratica}",{drzava},{grad})""")
        db.commit()
        clear()
        refreshTim()

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
####################################################


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

#PROZORI
root = Tk()
root.title("Baze podataka - Projekt")
root.geometry("500x500")




# NOTEBOOK
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=15)

# FRAMEOVI ( TABOVI )
frame = Frame(my_notebook, width=500, height=500, bg="blue")
frame2 = Frame(my_notebook, width=500, height=500, bg="red")
frame3 = Frame(my_notebook, width=500, height=500, bg="green")
frame4 = Frame(my_notebook, width=500, height=500, bg="yellow")
frame5 = Frame(my_notebook, width=500, height=500, bg="white")


# STAVLJANJE FRAME-ova NA GUI
frame.pack(fill="both", expand=1)
frame2.pack(fill="both", expand=1)
frame3.pack(fill="both", expand=1)
frame4.pack(fill="both", expand=1)
frame5.pack(fill="both", expand=1)


# ATRIBUTI FRAME-ova
my_notebook.add(frame, text="Igraci")
my_notebook.add(frame2, text="Treneri")
my_notebook.add(frame3, text="Sesije")
my_notebook.add(frame4, text="Sudci")
my_notebook.add(frame5, text="Timovi")

test_label = Label(frame5, text="No records to show", bg="white")
getTimovi()


#gumbi frame 5
dodaj_klub_gumb = Button(frame5, text="Dodaj tim", pady=5, command=dodajTim)
dodaj_klub_gumb.pack()



root.mainloop()
