from lukuvinkki import Lukuvinkki

class Vinkkikirjasto:

    def __init__(self):
        self.vinkit = []

    def esimerkki_vinkit(self):
        self.vinkit.append(Lukuvinkki("Helinä-keiju", "https://fi.wikipedia.org/wiki/Helinä-keiju"))
        self.vinkit.append(Lukuvinkki("Keijukainen", "https://fi.wikipedia.org/wiki/Keijukainen"))
        self.vinkit.append(Lukuvinkki("Keiju tuotteet", "https://www.keiju.fi/tuotteet/"))

    def hae_kaikki_vinkit(self):
        return self.vinkit

    def hea_viimeksi_lisatty_vinkki(self):
        return self.vinkit[-1]

    def lisaa_uusi_vinkki(self, otsikko, url):
        uusi_vinkki = Lukuvinkki(otsikko, url)
        self.vinkit.append(uusi_vinkki)

    def poista_kaikki_vinkit(self):
        self.vinkit.clear()
        