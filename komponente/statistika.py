
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *


def traziStatisiku(sesija_id):
    pokaziStatistiku = Tk()
    pokaziStatistiku.title("Podaci o sesiji")
    pokaziStatistiku.geometry("250x500")



    cursor.execute(f"SELECT * FROM statistika_opcenito WHERE id_sesija = {sesija_id}")
    rezultati = cursor.fetchall()

    label_id = Label(pokaziStatistiku, text=f"Podaci za sesiju [ID:{sesija_id}]")
    label_id.pack()

    for index, rezultat in enumerate(rezultati):
        test_label = Label(pokaziStatistiku, text=f" Tim1 ID: {rezultat[1]} \n Tim2 ID: {rezultat[2]} \n Tim1 Gol: {rezultat[3]} \n Tim2 Gol:{rezultat[4]} \n Tim1 posjed: {rezultat[5]} \n Tim2 posjed: {rezultat[6]} \n Tim1 out: {rezultat[7]} \n Tim2 out: {rezultat[8]} \n Tim1 udarci(ukupno): {rezultat[9]} \n Tim2 udarci(ukupno): {rezultat[10]} \n Tim1 udarci(u okvir): {rezultat[11]} \n Tim2 udarci(u okvir): {rezultat[12]}", bg="white")
        test_label.pack()