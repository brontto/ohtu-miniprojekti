from flask import (
    Flask,
    render_template,
    request,
    redirect
)
from vinkkikirjasto import Vinkkikirjasto


app = Flask(__name__)

vinkkikirjasto = Vinkkikirjasto()
vinkkikirjasto.esimerkki_vinkit()

@app.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    otsikko = request.form["otsikko"]
    url = "http://" + request.form["url"]
    print(url)
    vinkkikirjasto.lisaa_uusi_vinkki(otsikko, url)
    return redirect("/lukuvinkit")

@app.route("/kirjautuminen", methods=["POST"])
def kirjautuminen():
    # kayttajatunnus = request.form["kayttajatunnus"]
    # salasana = request.form["salasana"]

    # Tarkasta onko käyttäjää olemassa ja onko salasana oikein
    # Uudelleenohjaus takaisin etusivulle tai lukuvinkkeihin
    return redirect("/lukuvinkit")

@app.route("/lukuvinkit", methods=["GET"])
def render_lukuvinkit():
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("lukuvinkit.html", vinkkilista = vinkkilista)


@app.route("/", methods=["GET"])
def render_etusivu():
    return render_template("etusivu.html")
