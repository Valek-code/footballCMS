from komponente.sqlConnection import *
from tkinter import *
from tkinter import ttk

#puni selekciju gradova
def popuniGradIzbor(lista):

    cursor.execute("SELECT * FROM grad")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[1]}")


#puni selekciju drzava
def popuniDrzaveIzbor(lista):

    cursor.execute("SELECT * FROM drzava")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[1]}")

#puni selekciju timova
def popuniTimoveIzbor(lista):

    cursor.execute("SELECT * FROM tim")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[1]}")

#puni selekciju sudaca
def popuniSudceIzbor(lista):

    cursor.execute("SELECT * FROM sudac")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[0]}")

#puni selekciju stadiona
def popuniStadioneIzbor(lista):

    cursor.execute("SELECT * FROM stadion")
    rezultati = cursor.fetchall()
    for x in rezultati:
        lista.insert(END, f"{x[1]}")