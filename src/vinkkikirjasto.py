from lukuvinkki import Lukuvinkki
from vinkki_repository import vinkkirepositorio as default_vinkkirepo

class Vinkkikirjasto:

    def __init__(self, vinkkirepo=default_vinkkirepo):
        self.vinkit = vinkkirepo

    def hae_kaikki_vinkit(self):
        return self.vinkit.hae_kaikki_vinkit()

    def hae_viimeksi_lisatty_vinkki(self):
        return self.vinkit.hae_uusin_vinkki()

    def lisaa_uusi_vinkki(self, otsikko, url):
        if self.onko_otsikko_kelvollinen(otsikko):
            if self.onko_url_kelvollinen(url):
                uusi_vinkki = Lukuvinkki(otsikko, url)
                self.vinkit.lisaa_uusi_vinkki(uusi_vinkki)

    def poista_tama_vinkki(self, otsikko, url):#kesken
        for vinkki in self.vinkit:
            if vinkki.get_otsikko == otsikko and vinkki.get_linkki == url:
                self.vinkit.remove(vinkki)

    def poista_kaikki_vinkit(self):
        self.vinkit.poista_kaikki_vinkit()

    def onko_url_kelvollinen(self, url):
        url = url.strip()
        if len(url) < 8:
            return False
        if " " in url or "http://http" in url or not "." in url:
            return False
        return True

    def onko_otsikko_kelvollinen(self, otsikko):
        otsikko = otsikko.strip()
        if len(otsikko) > 0:
            return True
        return False
