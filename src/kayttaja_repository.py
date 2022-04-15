from db import db

class KayttajaRepository:
    def __init__(self):
        pass

    def lisaa_uusi_kayttaja(self, tunnus, salasana):
        sql = "INSERT INTO kayttajat(tunnus, salasana) \
            VALUES (:tunnus, :salasana)"
        db.session.execute(sql, {"tunnus": tunnus, "salasana": salasana})
        db.session.commit()

    def hae_kayttaja_tunnuksella(self, tunnus):
        sql = "SELECT id, tunnus, salasana FROM kayttajat WHERE tunnus=:tunnus"
        result = db.session.execute(sql, {"tunnus":tunnus})
        return result.fetchone()

    def hae_kayttajan_id(self, tunnus):
        sql = "SELECT id FROM kayttajat WHERE tunnus=:tunnus"
        result = db.session.execute(sql, {"tunnus":tunnus})
        kayttajan_id = result.fetchone().id
        return kayttajan_id

    def hae_kaikki_kayttajat(self):
        sql = "SELECT * FROM kayttajat"
        result = db.session.execute(sql)
        kayttajat = result.fetchall()
        return kayttajat

    def poista_kaikki(self):
        sql = "DELETE FROM kayttajat"
        db.session.execute(sql)
        db.session.commit()

kayttajarepositorio = KayttajaRepository()
