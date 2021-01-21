
from tkinter import *
from tkinter import ttk
import mysql.connector

from komponente.sqlConnection import *
from komponente.selekcije import *
from komponente.alertWindows import *
import pandas as pd
import xlsxwriter


def SpremiStatistikuTxt(sesija_id):

    desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

    if not sesija_id or sesija_id == '':
        alertWindow('Niste upisali sesiju')
        return
    try:
        # ime timova
        File_object = open(f"{desktop}\Podaci_o_sesiji{sesija_id}.txt", "w", encoding='utf8')
        cursor.execute(f'SELECT ime FROM tim WHERE id = (SELECT id_tim1 FROM sesija WHERE id = {sesija_id})')
        ime_tim1 = cursor.fetchone()
        cursor.execute(f'SELECT ime FROM tim WHERE id = (SELECT id_tim2 FROM sesija WHERE id = {sesija_id})')
        ime_tim2 = cursor.fetchone()
        # fetch ime i prezime
        cursor.execute(
            f"SELECT i.ime as Ime, i.prezime as Prezime FROM igrac as i where id_tim=(SELECT id_tim1 FROM sesija WHERE id = {sesija_id})")
        rezultati = cursor.fetchall()
        # upisuje se u file ime tima1
        File_object.write(f'Ime tima: {ime_tim1[0]} \n')
        File_object.write(f'-------------------------------------------------------- \n')
        # upisuju se imena i prezimena igraca tima 1
        for x in rezultati:
            File_object.write(f'Ime: {x[0]}, Prezime: {x[1]} \n')
        # fetcha se ime i prezime trenera
        cursor.execute(
            f'SELECT t.ime, t.prezime FROM trener AS t INNER JOIN tim AS tr ON tr.id = t.id_tim INNER JOIN sesija as s ON tr.id=id_tim1 WHERE s.id={sesija_id}')
        rezultati = cursor.fetchall()
        for x in rezultati:
            File_object.write(f'Trener: {x[0]} {x[1]} \n')
        File_object.write(f'-------------------------------------------------------- \n')

        cursor.execute(
            f'SELECT i.ime, i.prezime, COUNT(id_igrac) AS broj_golova_na_utakmici FROM gol AS g INNER JOIN igrac AS i ON i.id = g.id_igrac INNER JOIN tim AS t ON t.id = i.id_tim INNER JOIN sesija as s ON t.id=id_tim1 WHERE id_sesija = {sesija_id} GROUP BY t.ime ORDER BY g.id_tim;')
        rezultati = cursor.fetchall()
        if rezultati:
            File_object.write(f'IME PREZIME | Broj golova \n')
        else:
            File_object.write(f'Bez golova u ovoj utakmici \n')
        for x in rezultati:
            File_object.write(f'{x[0]} {x[1]} | {x[2]} \n')
        File_object.write(f'-------------------------------------------------------- \n')

        cursor.execute(
            f'SELECT i.ime, i.prezime, k.tip_kazne FROM kazne AS k INNER JOIN igrac AS i ON i.id = k.id_igrac INNER JOIN tim AS t ON t.id = i.id_tim INNER JOIN sesija as s ON t.id=id_tim1 WHERE k.id_sesija = {sesija_id}')
        rezultati = cursor.fetchall()
        if rezultati:
            File_object.write(f'IME PREZIME | Tip kazne \n')
        else:
            File_object.write(f'Bez kazni u ovoj utakmici \n')
        for x in rezultati:
            File_object.write(f'{x[0]}  {x[1]} | {x[2]} \n')

        File_object.write(f'-------------------------------------------------------- \n')

        cursor.execute(
            f'SELECT i.ime, i.prezime, u.ukupno AS "ukupan broj udaraca", u.u_okvir FROM udarci AS u INNER JOIN tim AS t ON t.id = u.id_tim INNER JOIN igrac AS i ON i.id = u.id_igrac INNER JOIN sesija AS s ON t.id=s.id_tim1 WHERE id_sesija = {sesija_id}')
        rezultati = cursor.fetchall()
        if rezultati:
            File_object.write(f'IME PREZIME | Ukupno udaraca | U okvir \n')
        else:
            File_object.write(f'Bez udaraca u ovoj utakmici \n')
        for x in rezultati:
            File_object.write(f'{x[0]}  {x[1]} | {x[2]}             | {x[3]} \n')
        File_object.write(f'\n \n \n')
        # tim2
        cursor.execute(
            f"SELECT i.ime as Ime, i.prezime as Prezime FROM igrac as i where id_tim=(SELECT id_tim2 FROM sesija WHERE id = {sesija_id})")
        rezultati = cursor.fetchall()
        File_object.write(f'{ime_tim2[0]} \n')
        File_object.write(f'-------------------------------------------------------- \n')
        for x in rezultati:
            File_object.write(f'Ime: {x[0]}, Prezime: {x[1]} \n')
        cursor.execute(
            f'SELECT t.ime, t.prezime FROM trener AS t INNER JOIN tim AS tr ON tr.id = t.id_tim INNER JOIN sesija as s ON tr.id=id_tim2 WHERE s.id={sesija_id}')
        rezultati = cursor.fetchall()
        for x in rezultati:
            File_object.write(f'Trener: {x[0]} {x[1]} \n')

        File_object.write(f'-------------------------------------------------------- \n')

        cursor.execute(
            f'SELECT i.ime, i.prezime, COUNT(id_igrac) AS broj_golova_na_utakmici FROM gol AS g INNER JOIN igrac AS i ON i.id = g.id_igrac INNER JOIN tim AS t ON t.id = i.id_tim INNER JOIN sesija as s ON t.id=id_tim2 WHERE id_sesija = {sesija_id} GROUP BY t.ime ORDER BY g.id_tim')
        rezultati = cursor.fetchall()
        if rezultati:
            File_object.write(f'IME PREZIME | Broj golova \n')
        else:
            File_object.write(f'Bez golova u ovoj utakmici \n')
        for x in rezultati:
            File_object.write(f'{x[0]} {x[1]} | {x[2]} \n')
        File_object.write(f'-------------------------------------------------------- \n')

        cursor.execute(
            f'SELECT i.ime, i.prezime, k.tip_kazne FROM kazne AS k INNER JOIN igrac AS i ON i.id = k.id_igrac INNER JOIN tim AS t ON t.id = i.id_tim INNER JOIN sesija as s ON t.id=id_tim2 WHERE k.id_sesija = {sesija_id}')
        rezultati = cursor.fetchall()
        if rezultati:
            File_object.write(f'IME PREZIME | Tip kazne \n')
        else:
            File_object.write(f'Bez kazni u ovoj utakmici \n')
        for x in rezultati:
            File_object.write(f'{x[0]}  {x[1]} | {x[2]} \n')
        File_object.write(f'-------------------------------------------------------- \n')

        cursor.execute(
            f'SELECT i.ime, i.prezime, u.ukupno AS "ukupan broj udaraca", u.u_okvir FROM udarci AS u INNER JOIN tim AS t ON t.id = u.id_tim INNER JOIN igrac AS i ON i.id = u.id_igrac INNER JOIN sesija AS s ON t.id=s.id_tim2 WHERE id_sesija = {sesija_id}')
        rezultati = cursor.fetchall()
        if rezultati:
            File_object.write(f'IME PREZIME | Ukupno udaraca | U okvir \n')
        else:
            File_object.write(f'Bez udaraca u ovoj utakmici \n')
        for x in rezultati:
            File_object.write(f'{x[0]}  {x[1]} | {x[2]}             | {x[3]} \n')
        File_object.write(f'-------------------------------------------------------- \n')
        # dohvacamo suca
        cursor.execute(
            f'SELECT s.ime, s.prezime FROM sudac AS s INNER JOIN sesija AS ses ON s.id = ses.id_sudac WHERE ses.id = {sesija_id}')
        rezultati = cursor.fetchall()
        for x in rezultati:
            File_object.write(f'Sudac: {x[0]} {x[1]} \n')
        alertWindow(f'Uspješno kreiran file "Podaci_o_sesija_{sesija_id}.txt" na radnoj površinu')
        File_object.close()
    except Exception as e:
        alertWindow(f'Došlo je do greške {e}')

# WORKBOOK / SHEET
def spremiStatistiku(sesija_id):

    desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

    if not sesija_id or sesija_id == '':
        alertWindow('Niste upisali sesiju')
        return
    try:
        workBook = xlsxwriter.Workbook(f'{desktop}\Podaci_sesija_{sesija_id}.xlsx')
        workSheet = workBook.add_worksheet()

        cursor.execute(f"SELECT * FROM sesija WHERE id = {sesija_id}")
        rezultati = cursor.fetchone()

        cursor.execute(f'SELECT COUNT(*) FROM gol WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
        golovi_tim1 = cursor.fetchone()

        cursor.execute(f'SELECT COUNT(*) FROM gol WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
        golovi_tim2 = cursor.fetchone()

        cursor.execute(f'SELECT ime FROM tim WHERE id = {rezultati[1]} ')
        ime_tim1 = cursor.fetchone()

        cursor.execute(f'SELECT ime FROM tim WHERE id = {rezultati[2]} ')
        ime_tim2 = cursor.fetchone()

        cursor.execute(
            f'SELECT IFNULL(SUM(broj_outova),0) FROM out_s JOIN sesija s ON {sesija_id} = s.id AND id_tim = s.id_tim1')
        outevi_tim1 = cursor.fetchone()

        outT1 = outevi_tim1[0]

        cursor.execute(
            f'SELECT IFNULL(SUM(broj_outova),0) FROM out_s JOIN sesija s ON {sesija_id} = s.id AND id_tim = s.id_tim2')
        outevi_tim2 = cursor.fetchone()

        outT2 = outevi_tim2[0]

        cursor.execute(
            f'SELECT IFNULL(SUM(ukupno),0) FROM udarci WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
        udarci_tim1 = cursor.fetchone()

        uT1 = udarci_tim1[0]

        cursor.execute(
            f'SELECT IFNULL(SUM(ukupno),0) FROM udarci WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
        udarci_tim2 = cursor.fetchone()

        cursor.execute(
            f'SELECT IFNULL(SUM(u_okvir),0) FROM udarci WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
        udarci_okvir_tim1 = cursor.fetchone()

        cursor.execute(
            f'SELECT IFNULL(SUM(u_okvir),0) FROM udarci WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
        udarci_okvir_tim2 = cursor.fetchone()

        cursor.execute(
            f'SELECT IFNULL(COUNT(id_igrac),0) FROM kazne WHERE id_tim = {rezultati[1]} AND id_sesija = {sesija_id}')
        kazne_tim1 = cursor.fetchone()


        cursor.execute(
            f'SELECT IFNULL(COUNT(id_igrac),0) FROM kazne WHERE id_tim = {rezultati[2]} AND id_sesija = {sesija_id}')
        kazne_tim2 = cursor.fetchone()

        cursor.execute(f"SELECT tr.ime, tr.prezime FROM trener tr JOIN tim t ON t.id = tr.id_tim WHERE t.ime = '{ime_tim1[0]}'")
        trenerT1 =  cursor.fetchone()

        cursor.execute(
            f"SELECT tr.ime, tr.prezime FROM trener tr JOIN tim t ON t.id = tr.id_tim WHERE t.ime = '{ime_tim2[0]}'")
        trenerT2 = cursor.fetchone()

        for index in range(1):
            workSheet.write('B1', 'Tim 1')
            workSheet.write('C1', 'Tim 2')

            workSheet.write('A1','Ime')
            workSheet.write('A3','Golovi')
            workSheet.write('A4','Outevi')
            workSheet.write('A5','Udarci u okvir')
            workSheet.write('A6','Udarci ukupno')
            workSheet.write('A7','Kazne')
            workSheet.write('A8','Treneri')
            workSheet.write('A10','Golovi: ')
            workSheet.write('H1','Igrač: ')
            workSheet.write('I1','Tim: ')


            workSheet.write('B10','Igrač')
            workSheet.write('C10','Minuta')
            workSheet.write('D10','Tim')


            workSheet.write('E1',F'ID_SESIJE: {sesija_id}')
            #workSheet.write('D1',F'Sudac_SESIJE: {sudacS}')


            workSheet.write('B1', ime_tim1[0])
            workSheet.write('B3', golovi_tim1[0])
            workSheet.write('B4', outevi_tim1[0])
            workSheet.write('B5', udarci_okvir_tim1[0])
            workSheet.write('B6', udarci_tim1[0])
            workSheet.write('B7', kazne_tim1[0])
            workSheet.write('B8', f'{trenerT1[0]} {trenerT1[1]}')

            workSheet.write('C1', ime_tim2[0])
            workSheet.write('C3', golovi_tim2[0])
            workSheet.write('C4', outevi_tim2[0])
            workSheet.write('C5', udarci_okvir_tim2[0])
            workSheet.write('C6', udarci_tim2[0])
            workSheet.write('C7', kazne_tim2[0])
            workSheet.write('C8', f'{trenerT2[0]} {trenerT2[1]}')


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
            results = cursor.fetchall()

            zadnji_x = 1
            zadnji_x_prez = 2
            zadnji_y = 10

            zadnji_y2 = 2

            for result in results:
                workSheet.write(zadnji_y, zadnji_x, result[1])
                workSheet.write(zadnji_y, zadnji_x_prez, result[2])
                workSheet.write(zadnji_y, zadnji_x_prez+1, result[0])
                zadnji_y = zadnji_y + 1


            cursor.execute(
                f'''
                SELECT CONCAT(i.ime,' ', i.prezime), t.ime FROM sesija s
                JOIN tim t ON t.id = s.id_tim1
                JOIN igrac i ON i.id_tim = t.id
                WHERE s.id = {sesija_id}
                UNION
                SELECT CONCAT(i.ime,' ', i.prezime), t.ime FROM sesija s
                JOIN tim t ON t.id = s.id_tim2
                JOIN igrac i ON i.id_tim = t.id
                WHERE s.id = {sesija_id};
                ''')

            igraciTimovi = cursor.fetchall()

            for r in igraciTimovi:
                workSheet.write(zadnji_y2, 7, r[0])
                workSheet.write(zadnji_y2, 8, r[1])
                zadnji_y2 = zadnji_y2 + 1

            workBook.close()
            alertWindow(f'Uspješno kreiran file "Podaci_sesija_{sesija_id}.xlsx" na radnoj površinu')
    except Exception as e:
        alertWindow(f'Došlo je do greške [{e}]')
        return

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
