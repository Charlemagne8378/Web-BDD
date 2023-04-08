from flask import render_template, Flask, request, flash, redirect, url_for
import sqlite3 

app = Flask(__name__)
app.secret_key="__key__"

def __init__(self):
    con = sqlite3.connect('database/user.db')
    c=con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS user(Nom, MDP)")
    con.commit()

@app.route("/")
def main(): 
    return render_template("index.html")

@app.route("/Inscription", methods=["POST","GET"])
def inscription(): 
    con=sqlite3.connect('database/user.db')
    c=con.cursor()
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if len(username) < 3: 
            flash('Votre nom est trop petit', category='error')
        elif len(password) < 6:
            flash('Votre mot de passe doit contenir plus de 6 caractères', category='error')
        else:
            statement = "SELECT * FROM user WHERE Nom=?"
            c.execute(statement, (username,))
            data = c.fetchone()
            if data:
                flash('Nom d\'utilisateur déjà utilisé', category='error')
            else:
                c.execute("INSERT INTO user (Nom, MDP) VALUES (?,?)",(username,password))
                con.commit()
                con.close()
                flash('Compte créé', category='success')
    else:
        return render_template("inscription.html")

    return render_template("inscription.html")

@app.route("/Connexion", methods=["POST","GET"])
def connexion(): 
    con = sqlite3.connect('database/user.db')
    c = con.cursor()
    if request.method=="POST":
        username = request.form.get('username')
        password = request.form.get('password')
        if len(username) < 3: 
            flash('Votre nom est trop petit', category='error')
        elif len(password) < 6:
            flash('Votre mot de passe doit contenir plus de 6 caractères', category='error')
        else:
            statement = "SELECT * FROM user WHERE Nom=? AND MDP=?"
            c.execute(statement, (username, password))
            data = c.fetchone()
            if data:
                return redirect(url_for('Admin'))
            else:
                flash('Nom d\'utilisateur ou mot de passe incorrect', category='error')
    else:
        return render_template("inscription.html")
    return render_template("connexion.html")


@app.route("/Objet")
def objet(): 
    return render_template("objet.html")   

@app.route("/Client")
def client(): 
    return render_template("client.html")    

@app.route("/Commande")
def commande(): 
    return render_template("lst_commande.html") 

@app.route("/Commander")
def commander(): 
    return render_template("commander.html") 

@app.route("/Admin")
def admin(): 
    return render_template("admin.html")     

@app.route("/à-propos")
def pro(): 
    return render_template("à-propos.html")

app.run(debug=True)

