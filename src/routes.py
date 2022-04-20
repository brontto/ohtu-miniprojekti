from flask import request, redirect, render_template, session
from vinkkikirjasto import Vinkkikirjasto
from kayttajat import Kayttajat
from app import app


vinkkikirjasto = Vinkkikirjasto()
kayttajat = Kayttajat()

@app.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    otsikko = request.form["otsikko"]
    url = request.form["url"]
    kayttaja_id = session.get("kayttaja_id", 0)
    vinkkikirjasto.lisaa_uusi_vinkki(otsikko, url, kayttaja_id)
    return redirect("/lukuvinkit")

@app.route("/kirjautuminen", methods=["POST"])
def kirjautuminen():
    tunnus = request.form["kayttajatunnus"]
    salasana = request.form["salasana"]

    kayttaja = kayttajat.kirjaudu_sisaan(tunnus, salasana)
    if not kayttaja:
        error = "Käyttäjätunnus tai salasana väärin"
        return render_etusivu(error)

    kayttaja_id = kayttaja.id
    kayttajat.aseta_sessio(tunnus, kayttaja_id)

    return redirect("/lukuvinkit")

@app.route("/kirjaudu_ulos")
def kirjaudu_ulos():
    kayttajat.kirjaudu_ulos()
    return redirect("/")

@app.route("/rekisterointi", methods=["GET"])
def rekisterointi():
    return render_template("rekisterointi.html")

@app.route("/luo_uusi_kayttaja", methods=["POST"])
def luo_uusi_kayttaja():
    kayttajatunnus = request.form["kayttajatunnus"]
    salasana = request.form["salasana"]
    salasana2 = request.form["salasana_varmistus"]

    if not salasana:
        error = "Tarvitset myös salasanan"
        return render_template("rekisterointi.html", error=error) 
    
    if not salasana == salasana2:
        error = "Salasanat eivät täsmää"
        return render_template("rekisterointi.html", error=error)

    if not kayttajat.lisaa_uusi_kayttaja(kayttajatunnus, salasana):
        error = "käyttäjätunnus on jo olemassa"
        return render_template("rekisterointi.html", error=error)

    kayttaja = kayttajat.kirjaudu_sisaan(kayttajatunnus, salasana)
    kayttaja_id = kayttaja.id

    kayttajat.aseta_sessio(kayttajatunnus, kayttaja_id)

    return redirect("/lukuvinkit")

@app.route("/lukuvinkit", methods=["GET"])
def render_lukuvinkit():
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("lukuvinkit.html", vinkkilista=vinkkilista)

@app.route("/")
def render_etusivu(error=None):
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("etusivu.html", vinkkilista=vinkkilista, error=error)

@app.route("/tyhjenna_tietokannat")
def reset_database():
    kayttajat.poista_kaikki_kayttajat()
    vinkkikirjasto.poista_kaikki_vinkit()
    return redirect("/")

@app.route("/ping")
def ping():
    return "pong"
    
