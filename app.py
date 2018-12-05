
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bcrypt import check_password_hash
from flask_login import LoginManager, login_user, login_required
from db import DB
from DataLoader import Loader

app = Flask(__name__)
app.debug = True
app.secret_key = "90nljlx9us0jsxj898xk.4.$sfadsev90<8fsh"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return database.read_user_by_id(user_id)


alleKantone = {"ZH" : "Zürich",
               "BE" : "Bern",
                "LU" : "Luzern",
                "UR" : "Uri",
                "SZ" : "Schwyz",
                "OW" : "Obwalden",
                "NW" : "Nidwalden",
                "GL" : "Glarus",
                "ZG" : "Zug",
                "FR" : "Freiburg",
                "SO" : "Solothurn",
                "BS" : "Basel-Stadt",
                "BL" : "Basel-Landschaft",
                "SH" : "Schaffhausen",
                "AR" : "Appenzell Ausserrhoden",
                "AI" : "Appenzell Innerrhoden",
                "SG" : "St. Gallen",
                "GR" : "Graubünden",
                "AG" : "Aargau",
                "TG" : "Thurgau",
                "TI" : "Tessin",
                "VD" : "Waadt",
                "VS" : "Wallis",
                "NE" : "Neuenburg",
                "GE" : "Genf",
                "JU" : "Jura"
               }

@app.route("/")
def index():
    return render_template("indexmin.html")

@app.route("/kantone")
def kantone():
    return render_template("kantone.html", kantone = alleKantone)

@app.route("/kantone/<kanton>")
def kanton(kanton):
    berge = database.read_mountains_by_kanton(kanton)
    return render_template("kanton.html", kanton = alleKantone[kanton.upper()], berge = berge)

@app.route("/<berg>")
def berg(berg):
    berg = database.read_mountain_by_name(berg)
    return render_template("berg.html", berg = berg)

@app.route("/suche")
def suche():
    return render_template("suche.html", kantone = alleKantone)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = database.read_user(username)
        if user and check_password_hash(user.password, password):
            if user.is_activated:
                login_user(user)
                return redirect(url_for("kantone"))
            else:
                flash("User needs to be activated from the administrator. Please be patient.")
                return redirect(url_for("index"))
        else:
            flash("Ungültige Kombination von Benutzername und Passwort. Bitte versuche es erneut.")
            return render_template("login.html")
    else:
        return render_template("login.html")

if __name__ == "__main__":
    database = DB()
    #database.create()
    database.create_tables()
    database.connect()
    #data_loader = Loader(database)
    #data_loader.create_admin_user()
    #data_loader.create_mountains()

    #Local
    app.run(host='127.0.0.1', port=80)

    #Server
    #app.run(host='0.0.0.0', port=80)
