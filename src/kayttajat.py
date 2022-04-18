from secrets import token_hex
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session
from sqlalchemy import exc
from kayttaja_repository import kayttajarepositorio as default_kayttajarepo


class Kayttajat:

    def __init__(self, kayttajarepo=default_kayttajarepo):
        self.kayttajat = kayttajarepo

    def lisaa_uusi_kayttaja(self, tunnus, salasana):
        try:
            salasana_hash = generate_password_hash(salasana)
            self.kayttajat.lisaa_uusi_kayttaja(tunnus, salasana_hash)
        except exc.IntegrityError:
            return False
        return True

    def hae_kayttaja(self, tunnus):
        return self.kayttajat.hae_kayttaja_tunnuksella(tunnus)

    def hae_kaikki_kayttajat(self):
        return self.kayttajat.hae_kaikki_kayttajat()

    def poista_kaikki_kayttajat(self):
        self.kayttajat.poista_kaikki()

    def kirjaudu_sisaan(self, tunnus, salasana):
        kayttaja = self.hae_kayttaja(tunnus)

        if not kayttaja:
            return None
        if not self.salasana_oikein(kayttaja, salasana):
            return None
        return kayttaja

    def aseta_sessio(self, tunnus, kayttaja_id):
        session["tunnus"] = tunnus
        session["kayttaja_id"] = kayttaja_id
        session["csrf_token"] = token_hex(16)

    def salasana_oikein(self, kayttaja, salasana):
        salasana_hash = kayttaja[2]
        return check_password_hash(salasana_hash, salasana)

    def kirjaudu_ulos(self):
        if session["tunnus"]:
            del session["tunnus"]
            del session["kayttaja_id"]
            del session["csrf_token"]


kayttajat = Kayttajat()
