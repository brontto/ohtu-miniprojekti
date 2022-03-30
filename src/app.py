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

@app.route("/", methods=["GET"])
def render_etusivu():
    vinkkilista = vinkkikirjasto.hae_kaikki_vinkit()
    return render_template("index.html", vinkkilista = vinkkilista)

@app.route("/luo_vinkki", methods=["POST"])
def luo_vinkki():
    otsikko = request.form["otsikko"]
    url = "http://" + request.form["url"]
    print(url)
    vinkkikirjasto.lisaa_uusi_vinkki(otsikko, url)
    return redirect("/")
