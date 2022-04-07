from db import db

class VinkkiRepository:
    def __init__(self):
        pass

    def lisaa_uusi_vinkki(self, vinkki):
        sql = "INSERT INTO lukuvinkit (otsikko, linkki, kayttaja_id) \
            VALUES (:otsikko, :linkki, 1)"

        db.session.execute(sql, {"otsikko": vinkki.get_otsikko(),
            "linkki": vinkki.get_linkki()})
        db.session.commit()

    def hae_uusin_vinkki(self):
        sql = "SELECT otsikko, linkki MAX(id) FROM lukuvinkit"
        result = db.session.execute(sql)
        uusin = result.fetchone()
        return uusin

    def hae_kaikki_vinkit(self):
        sql = "SELECT otsikko, linkki FROM lukuvinkit"
        result = db.session.execute(sql)
        vinkit = result.fetchall()
        return vinkit

    def poista_kaikki_vinkit(self):
        sql = "DELETE FROM lukuvinkit"
        db.session.execute(sql)
        db.session.commit()

vinkkirepositorio = VinkkiRepository()
