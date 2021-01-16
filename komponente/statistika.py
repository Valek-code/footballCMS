
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


    cursor.execute(f"SELECT * FROM sesija WHERE id = {sesija_id}")
    rezultati = cursor.fetchone()

    label_id = Label(pokaziStatistiku, text=f"Podaci za sesiju [ID:{sesija_id}]")
    label_id.pack()

    if not rezultati:
        print('TRUE')
        test_label2 = Label(pokaziStatistiku, text='Nema podataka za ovu sesiju!', bg="white")
        test_label2.pack()
        return

    cursor.execute(f'SELECT COUNT(*) FROM gol WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    golovi_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT COUNT(*) FROM gol WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    golovi_tim2 = cursor.fetchone()

    cursor.execute(f'SELECT broj_outova FROM out_s WHERE id_tim1 = {rezultati[1]} AND id_sesija = {sesija_id}')
    outevi_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT broj_outova FROM out_s WHERE id_tim1 = {rezultati[1]} AND id_sesija = {sesija_id}')
    outevi_tim2 = cursor.fetchone()

    cursor.execute(f'SELECT ukupno FROM udarci WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    udarci_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT ukupno FROM udarci WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    udarci_tim2 = cursor.fetchone()

    cursor.execute(f'SELECT COUNT(*) FROM kazne WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    kazne_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT COUNT(*) FROM kazne WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    kazne_tim2 = cursor.fetchone()

    for index in range(1):
        print('FALSE')
        test_label = Label(pokaziStatistiku, text=f" Tim1 ID: {rezultati[1]} \n Tim2 ID: {rezultati[2]} \n Golovi: TIM1[ {golovi_tim1[0]} ] - TIM2[ {golovi_tim2[0]} ] \n Outs: TIM1[ {outevi_tim1[0]} ] - TIM2[ {outevi_tim2[0]} ] \n Udarci: TIM1[ {udarci_tim1[0]} ] - TIM2[ {udarci_tim2[0]} ] \n Kazne : TIM1[ {kazne_tim1[0]} ] - TIM2[ {kazne_tim2[0]} ] \n ", bg="white")
        test_label.pack()

