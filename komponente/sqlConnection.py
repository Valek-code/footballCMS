import mysql.connector
import os
import sys
from configparser import ConfigParser

config = ConfigParser()
file = os.path.join(os.path.dirname(__file__),"config.ini")

config.read(file)

host = config.get('sqlAccount', 'host')
username = config.get('sqlAccount', 'username')
password = config.get('sqlAccount', 'password')
db_name = config.get('sqlAccount', 'db')



# otvaranje veze s lokalnom bazom podataka
db = mysql.connector.connect(
    host=f"{host}",
    user=f"{username}", # user na koji se spaja
    auth_plugin='mysql_native_password', # don't touch prekidach
    passwd=f"{password}", # loznika vaseg user-a u database ( vrlo vjerojatno lozinka root user-a )
    db=f"{db_name}" # naziv sheme/baze
)

cursor = db.cursor() # cursor koji dohvaca podatke iz baze
                     # u globalu je cisto da se moze koristiti bilo gdje unutar koda
cursor2 = db.cursor()

