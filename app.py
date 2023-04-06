# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, Flask

app = Flask(__name__)

@app.route("/")
def main(): 
    return render_template("index.html")

@app.route("/Objet")
def objet(): 
    return render_template("objet.html")   

@app.route("/Client")
def client(): 
    return render_template("client.html")    

@app.route("/Commande")
def commande(): 
    return render_template("commande.html")       

@app.route("/Connexion")
def connexion(): 
    return render_template("connexion.html")    

@app.route("/Admin")
def admin(): 
    return render_template("admin.html")     

@app.route("/à-propos")
def pro(): 
    return render_template("à-propos.html")

app.run(debug=True)

