
from os import getenv
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    redirect

)
from werkzeug.security import generate_password_hash
from db import db

from vinkkikirjasto import Vinkkikirjasto
from kayttajat import Kayttajat

app = Flask(__name__)

load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db.init_app(app)

vinkkikirjasto = Vinkkikirjasto()
kayttajat= Kayttajat()

@app.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    otsikko = request.form["otsikko"]
    url = "http://" + request.form["url"]
    vinkkikirjasto.lisaa_uusi_vinkki(otsikko, url)
    return redirect("/lukuvinkit")

@app.route("/kirjautuminen", methods=["POST"])
def kirjautuminen():
    kayttajatunnus = request.form["kayttajatunnus"]
    salasana = request.form["salasana"]
    print(kayttajatunnus, salasana)

    # Tarkasta onko käyttäjää olemassa ja onko salasana oikein
    # Uudelleenohjaus takaisin etusivulle tai lukuvinkkeihin
    return redirect("/lukuvinkit")

@app.route("/rekisterointi", methods=["GET"])
def rekisterointi():
    return render_template("rekisterointi.html")

@app.route("/luo_uusi_kayttaja", methods=["POST"])
def luo_uusi_kayttaja():
    kayttajatunnus = request.form["kayttajatunnus"]
    salasana = request.form["salasana"]
    salasana2 = request.form["salasana_varmistus"]
    if salasana == salasana2:
        hash_salasana = generate_password_hash(salasana)
        kayttajat.lisaa_uusi_kayttaja(kayttajatunnus,hash_salasana)

    print(kayttajatunnus,salasana,salasana2)
    #Tarkastetaan että kentät ei ole tyhjiä ja että salasanat täsmäävät
    #Tarkistetaan että nimi ei ole käytössä
    #printataan kayttajatunnus,salasana ja salasana2 jottei pylint huuda käyttämättömistä muuttujista
    return redirect("/")

@app.route("/lukuvinkit", methods=["GET"])
def render_lukuvinkit():
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("lukuvinkit.html", vinkkilista = vinkkilista)

@app.route("/")
def render_etusivu():
    return render_template("etusivu.html")
