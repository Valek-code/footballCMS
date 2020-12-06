import mysql.connector

# otvaranje veze s lokalnom bazom podataka
db = mysql.connector.connect(
    host="localhost",
    user="user", # user na koji se spaja
    auth_plugin='mysql_native_password', # don't touch prekidach
    passwd="V#l3k698", # loznika vaseg user-a u database ( vrlo vjerojatno lozinka root user-a )
    db="projekt" # naziv sheme/baze
)

cursor = db.cursor() # cursor koji dohvaca podatke iz baze
                     # u globalu je cisto da se moze koristiti bilo gdje unutar koda
cursor2 = db.cursor()

