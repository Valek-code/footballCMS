
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *



def traziStatisiku(sesija_id):
    pokaziStatistiku = Tk()
    pokaziStatistiku.title("Podaci o sesiji")
    pokaziStatistiku.geometry("300x300")


    cursor.execute(f"SELECT * FROM sesija WHERE id = {sesija_id}")
    rezultati = cursor.fetchone()

    label_id = Label(pokaziStatistiku, text=f"Podaci za sesiju [ID:{sesija_id}]")
    label_id.pack()

    if not sesija_id or sesija_id == '':
        label_id2 = Label(pokaziStatistiku, text=f"Podaci za sesiju ne postoje")
        label_id2.pack()
        return

    if not rezultati or rezultati == '':
        print('TRUE')
        test_label2 = Label(pokaziStatistiku, text='Nema podataka za ovu sesiju!', bg="white")
        test_label2.pack()
        return
    cursor.execute(f'SELECT COUNT(*) FROM gol WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    golovi_tim1 = cursor.fetchone()


    cursor.execute(f'SELECT COUNT(*) FROM gol WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    golovi_tim2 = cursor.fetchone()


    cursor.execute(f'SELECT ime FROM tim WHERE id = {rezultati[1]} ')
    ime_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT ime FROM tim WHERE id = {rezultati[2]} ')
    ime_tim2 = cursor.fetchone()


    cursor.execute(f'SELECT IFNULL(SUM(broj_outova),0) FROM out_s JOIN sesija s ON {sesija_id} = s.id AND id_tim = s.id_tim1')
    outevi_tim1 = cursor.fetchone()

    outT1 = outevi_tim1[0]

    cursor.execute(f'SELECT IFNULL(SUM(broj_outova),0) FROM out_s JOIN sesija s ON {sesija_id} = s.id AND id_tim = s.id_tim2')
    outevi_tim2 = cursor.fetchone()

    outT2 = outevi_tim2[0]

    cursor.execute(f'SELECT IFNULL(SUM(ukupno),0) FROM udarci WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    udarci_tim1 = cursor.fetchone()

    uT1 = udarci_tim1[0]

    cursor.execute(f'SELECT IFNULL(SUM(ukupno),0) FROM udarci WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    udarci_tim2 = cursor.fetchone()

    cursor.execute(f'SELECT IFNULL(SUM(u_okvir),0) FROM udarci WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    udarci_okvir_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT IFNULL(SUM(u_okvir),0) FROM udarci WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    udarci_okvir_tim2 = cursor.fetchone()

    cursor.execute(f'SELECT IFNULL(COUNT(id_igrac),0) FROM kazne WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
    kazne_tim1 = cursor.fetchone()

    cursor.execute(f'SELECT IFNULL(COUNT(id_igrac),0) FROM kazne WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
    kazne_tim2 = cursor.fetchone()




    uT2 = udarci_tim2[0] or 0

    for index in range(1):
        test_label = Label(pokaziStatistiku, text=f" Tim1 : {ime_tim1[0]} \n Tim2 : {ime_tim2[0]} \n Golovi: TIM1[ {golovi_tim1[0]} ] - TIM2[ {golovi_tim2[0]} ] \n Outevi: TIM1[ {outT1} ] - TIM2[ {outT2} ] \n Udarci: TIM1[ {uT1}({udarci_okvir_tim1[0]}) ] - TIM2[ {udarci_tim2[0]}({udarci_okvir_tim1[0]}) ] \n Kazne : TIM1[ {kazne_tim1[0]} ] - Tim2 [ {kazne_tim2[0]} ]", bg="white")
        test_label.pack()


    cursor.execute(f'''
        SELECT t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', TIMESTAMPDIFF(MINUTE, g.vrijeme, s.datum_sesija) * -1 as vrijeme FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
        JOIN gol g ON i.id = g.id_igrac
		WHERE s.id = {sesija_id}
	UNION
	SELECT t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac', TIMESTAMPDIFF(MINUTE, g.vrijeme, s.datum_sesija) * -1 as vrijeme FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
        JOIN gol g ON i.id = g.id_igrac
		WHERE s.id = {sesija_id};
    
    ''')

    test_label3 = Label(pokaziStatistiku, text=f'GOLOVI: ')
    test_label3.pack()
    rezultati = cursor.fetchall()
    for rezultat in rezultati:
        test_label2 = Label(pokaziStatistiku, text=f"[{+int(rezultat[2])}'] - {rezultat[1]} - {rezultat[0]} ",bg='white')
        test_label2.pack()