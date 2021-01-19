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


#puni selekciju stadiona
def popuniIgraceIzbor(lista, id_sesija):

    cursor2.execute(f"""
    SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac' FROM sesija s
		JOIN tim t ON t.id = s.id_tim1
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = {id_sesija}
	UNION
	SELECT i.id,t.ime ime_tima,CONCAT(i.ime,' ', i.prezime) as 'Igrac' FROM sesija s
		JOIN tim t ON t.id = s.id_tim2
		JOIN igrac i ON i.id_tim = t.id
		WHERE s.id = {id_sesija}
""")
    rezultati = cursor2.fetchall()
    for x in rezultati:
        lista.insert(END, f"ID[{x[0]}] | TIM [ > {x[1]} < ] - {x[2]}")