#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, request,redirect
import numpy as np
import pandas as pd
import os
import sqlite3 as sql
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/sauvegarde'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    fpseudo = str(fpseudo)
    fsex = request.form['sex']
    if fsex == "M":
        ab="Mr"
    else :
        ab="Mme"
    with sql.connect("pflask.db") as con:
        cur = con.cursor()
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select pseudo from utilisateurs where pseudo=?",[fpseudo])
        rows = cur.fetchall()
        nb=len(rows)
        if nb == 0 :
            cur.execute("INSERT INTO utilisateurs (nom,prenom,pseudo,sexe)VALUES (?,?,?,?)",(fnom,fprenom,fpseudo,fsex) )
            con.commit()
            msg = "Enregistrement reussi"
        else :
            msg = "Enregistrement impossible"
            return render_template("refus.html", nom=fnom,prenom=fprenom,pseudo=fpseudo,ab=ab,msg=msg)
    return render_template("bienvenue.html", nom=fnom,prenom=fprenom,pseudo=fpseudo,ab=ab,msg=msg)

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        nom_fichier = f.filename
        nom_fichier = secure_filename(nom_fichier)
        f.save('./sauvegarde/' + nom_fichier)
        result_f='fichier telecharge'
        data =  pd.read_csv('./sauvegarde/'+ nom_fichier, sep=',')
        data5=data.head(5)
        stats_f = data.describe()
    return render_template('upload.html', msg_f=result_f,nom_f=nom_fichier,tables=[stats_f.to_html(classes='statist'),data5.to_html(classes='data')],titles = ['na', 'statistiques','les 5 premieres lignes du jeu de donnees'])


@app.route('/perdu')
def perdu():
    return render_template('perdu.html', titre="Bienvenue !")

@app.route('/', methods=['POST'])
def login():
    text = request.form['username']
    processed_text = text.upper()
    return render_template("bienvenue.html", message=processed_text)

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
