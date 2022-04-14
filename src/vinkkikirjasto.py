from sqlalchemy import false, true
from lukuvinkki import Lukuvinkki
from vinkki_repository import vinkkirepositorio as default_vinkkirepo

class Vinkkikirjasto:

    def __init__(self, vinkkirepo=default_vinkkirepo):
        self.vinkit = vinkkirepo

    # def esimerkki_vinkit(self):
    #     self.testivinkit.append(Lukuvinkki("Helinä-keiju", "https://fi.wikipedia.org/wiki/Helinä-keiju"))
    #     self.testivinkit.append(Lukuvinkki("Keijukainen", "https://fi.wikipedia.org/wiki/Keijukainen"))
    #     self.testivinkit.append(Lukuvinkki("Keiju tuotteet", "https://www.keiju.fi/tuotteet/"))

    def hae_kaikki_vinkit(self):
        return self.vinkit.hae_kaikki_vinkit()

    def hae_viimeksi_lisatty_vinkki(self):
        return self.vinkit.hae_uusin_vinkki()

    def lisaa_uusi_vinkki(self, otsikko, url):
        if self.onko_otsikko_kelvollinen(otsikko) == True and self.onko_url_kelvollinen(url) == True:
            uusi_vinkki = Lukuvinkki(otsikko, url)
            self.vinkit.lisaa_uusi_vinkki(uusi_vinkki)
        
    def poista_kaikki_vinkit(self):
        self.vinkit.poista_kaikki_vinkit()
        
    def onko_url_kelvollinen(self, url):# ei välilyöntejä, ei symboleita, kuten &% ei kenoviivoja \ 
        url = url.strip()
        if len(url)>7:
            for character in url:
                if character == " ":
                    return False
            if "http://http" in url:
                return False
            if not "." in url:
                return False
            return True
     
    def onko_otsikko_kelvollinen(self, otsikko): 
        otsikko = otsikko.strip()
        if len(otsikko)!=0:
            return True
        