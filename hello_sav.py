#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('accueil.html', titre="Bienvenue !")

@app.route('/', methods=['POST'])
def text_box():
    fnom = request.form['nom']
    fnom = fnom.upper()
    fprenom = request.form['prenom']
    fprenom = fprenom.capitalize()
    fpseudo = request.form['pseudo']
    fsex = request.form['sex']
    if fsex == "M":
        ab="Mr"
    else :
        ab="Mme"
    with sql.connect("pflask.db") as con:
        cur = con.cursor()
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from utilisateurs where pseudo=?",(fpseudo))
        rows = cur.fetchall()
        nb=len(rows)
        if nb == 0 :
            cur.execute("INSERT INTO utilisateurs (nom,prenom,pseudo,sexe)VALUES (?,?,?,?)",(fnom,fprenom,fpseudo,fsex) )
            con.commit()
            msg = "Enregistrement reussi"
        else :
            msg = "Enregistrement impossible"
    return render_template("bienvenue.html", nom=fnom,prenom=fprenom,pseudo=fpseudo,ab=ab,msg=msg)

@app.route('/perdu')
def perdu():
    return render_template('perdu.html', titre="Bienvenue !")

@app.route('/liste')
def liste():
    con = sql.connect("pflask.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from utilisateurs")
    rows = cur.fetchall()
    return render_template("liste_ab.html",rows = rows)


if __name__ == '__main__':
    app.run(debug=True)
