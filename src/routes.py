from flask import request, redirect, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from vinkkikirjasto import Vinkkikirjasto
from kayttajat import Kayttajat
from app import app


vinkkikirjasto = Vinkkikirjasto()
kayttajat = Kayttajat()

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
    kayttaja = kayttajat.tarkasta_kayttajatunnus(kayttajatunnus)

    if not kayttaja:
        print("Käyttäjätunnus on väärin")
        return redirect("/")

    hash_value = kayttaja.salasana
    if check_password_hash(hash_value, salasana):
        print("Kirjauduttu sisään")
        return redirect("/lukuvinkit")
    print("Salasana on väärin")
    return redirect("/")

@app.route("/rekisterointi", methods=["GET"])
def rekisterointi():
    return render_template("rekisterointi.html")

@app.route("/luo_uusi_kayttaja", methods=["POST"])
def luo_uusi_kayttaja():
    kayttajatunnus = request.form["kayttajatunnus"]
    salasana = request.form["salasana"]
    salasana2 = request.form["salasana_varmistus"]

    tunnus_olemassa = kayttajat.tarkasta_kayttajatunnus(kayttajatunnus)

    if tunnus_olemassa:
        error = "käyttäjätunnus on jo olemassa"
        return render_template("rekisterointi.html", error=error)

    if salasana == salasana2:
        hash_salasana = generate_password_hash(salasana)
        kayttajat.lisaa_uusi_kayttaja(kayttajatunnus,hash_salasana)
    return redirect("/")

@app.route("/lukuvinkit", methods=["GET"])
def render_lukuvinkit():
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("lukuvinkit.html", vinkkilista = vinkkilista)

@app.route("/")
def render_etusivu():
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("etusivu.html", vinkkilista = vinkkilista)
    