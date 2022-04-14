from secrets import token_hex
from werkzeug.security import check_password_hash
from flask import session
from kayttaja_repository import kayttajarepositorio as default_kayttajarepo


class Kayttajat:

    def __init__(self, kayttajarepo=default_kayttajarepo):
        self.kayttajat = kayttajarepo

    def lisaa_uusi_kayttaja(self, tunnus, salasana):
        return self.kayttajat.lisaa_uusi_kayttaja(tunnus, salasana)

    def tarkasta_kayttajatunnus(self, tunnus):
        return self.kayttajat.tarkasta_sisaankirjautuminen(tunnus)

    def hae_kaikki_kayttajat(self):
        return self.kayttajat.hae_kaikki_kayttajat()

    def kirjaudu_sisaan(self, tunnus, salasana):
        kayttaja = self.tarkasta_kayttajatunnus(tunnus)

        if not kayttaja:
            return False
        if not check_password_hash(kayttaja[2], salasana):
            return False

        session["tunnus"] = tunnus
        session["kayttaja_id"] = kayttaja[0]
        session["csrf_token"] = token_hex(16)

        return True

    def kirjaudu_ulos(self):
        del session["tunnus"]
        del session["kayttaja_id"]
        del session["csrf_token"]

kayttajat = Kayttajat()
