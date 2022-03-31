from vinkkikirjasto import Vinkkikirjasto

class VinkkikirjastoLibrary:
    def __init__(self):
        self._vinkkikirjasto = Vinkkikirjasto()
    
        
    def lisaa_uusi_vinkki(self, otsikko, url):
        self._vinkkikirjasto.lisaa_uusi_vinkki(otsikko,url)
        
    def uuden_vinkin_otsikko_pitaisi_olla(self, otsikko):
        viimeisin_otsikko = self._vinkkikirjasto.hea_viimeksi_lisatty_vinkki().get_otsikko()
        if viimeisin_otsikko != otsikko:
            raise AssertionError(f"{viimeisin_otsikko} != {otsikko}")