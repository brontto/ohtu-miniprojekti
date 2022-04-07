from lukuvinkki import Lukuvinkki
from vinkki_repository import vinkki_repositorio

class Vinkkikirjasto:

    def __init__(self):
        self.vinkit = vinkki_repositorio
        self.testivinkit = []

    def esimerkki_vinkit(self):
        self.testivinkit.append(Lukuvinkki("Helinä-keiju", "https://fi.wikipedia.org/wiki/Helinä-keiju"))
        self.testivinkit.append(Lukuvinkki("Keijukainen", "https://fi.wikipedia.org/wiki/Keijukainen"))
        self.testivinkit.append(Lukuvinkki("Keiju tuotteet", "https://www.keiju.fi/tuotteet/"))

    def hae_kaikki_vinkit(self):
        return self.testivinkit

    def hae_viimeksi_lisatty_vinkki(self):
        return self.testivinkit[-1]

    def lisaa_uusi_vinkki(self, otsikko, url):
        uusi_vinkki = Lukuvinkki(otsikko, url)
        self.vinkit.lisaa_uusi_vinkki(uusi_vinkki)

    def poista_kaikki_vinkit(self):
        self.testivinkit.clear()
        