# lisää uusi käyttäjä
from kayttaja_repository import kayttajarepositorio as default_kayttajarepo

class Kayttajat:

    def __init__(self, kayttajarepo=default_kayttajarepo):
        self.kayttajat = kayttajarepo

    def lisaa_uusi_kayttaja(self, tunnus, salasana):
        self.kayttajat.lisaa_uusi_kayttaja(tunnus, salasana)

    def tarkasta_kayttajatunnus(self, tunnus):
        return self.kayttajat.tarkasta_sisaankirjautuminen(tunnus)
        