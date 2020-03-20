from flask import Flask, render_template, request
import sqlite3 as sql
fnom='CATALAN'
fprenom='Davy'
conn = sql.connect('pflask.db')
print ("Opened database successfully")
#conn.execute('DROP TABLE utilisateurs')
#conn.execute('CREATE TABLE utilisateurs (nom,prenom,pseudo,sexe)')
con = sql.connect("pflask.db")
con.row_factory = sql.Row
cur = con.cursor()
cur.execute("select * from utilisateurs")
rows = cur.fetchall()
nb=len(rows)
print (f"nombre de ligne {nb}")
conn.close()